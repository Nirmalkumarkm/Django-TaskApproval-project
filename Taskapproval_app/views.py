# Taskapproval_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task, TaskCompletion, Department
from .forms import TaskForm
from django.urls import reverse

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            
            # Check if the task is completed and belongs to DEPT 1
            if task.status == 'Completed' and task.department.name == 'DEPT 1':
                # Automatically create a task for DEPT 2
                dept2 = Department.objects.get(name='DEPT 2')
                Task.objects.create(
                    name=f"Automatically created for DEPT 2 upon completion of {task.name}",
                    description=task.description,
                    department=dept2,
                    user=None,  # Assign to a user later as per your logic
                    status='Pending'
                )
                
            messages.success(request, 'Task created successfully.')
            return redirect(reverse('task_list'))
    else:
        form = TaskForm()
    
    return render(request, 'Taskapproval_app/create_task.html', {'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    print(tasks)
    return render(request, 'Taskapproval_app/task_list.html', {'tasks': tasks})

@login_required
def task_report(request):
    tasks = Task.objects.all()
    return render(request, 'Taskapproval_app/task_report.html', {'tasks': tasks})


