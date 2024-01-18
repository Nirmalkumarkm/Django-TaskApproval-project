from django.shortcuts import render 

def create_task(request):
    return render(request, 'create_task.html')

def task_list(request):
    return render(request, 'task_list.html')

def task_report(request):
    return render(request, 'task_report.html')






