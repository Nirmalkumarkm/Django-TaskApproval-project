"""
URL configuration for Task_Approval project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# task_approval/urls.py
from django.urls import path
from .views import create_task, task_list, task_report

urlpatterns = [
    path('create-task/', create_task, name='create_task'),
    path('task-list/', task_list, name='task_list'),
    path('task-report/', task_report, name='task_report'),
]


