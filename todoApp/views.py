from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def todoView(request):
    task_obj = TodoModel.objects.all()
    dict1 = {'task_obj': task_obj}
    return render(request, "todoApp/home.html", dict1)


def addTask(request):
    mytask = request.POST['task']
    TodoModel(task = mytask).save()
    return redirect(request.META["HTTP_REFERER"])


def deleteTask(request, taskID):
    TodoModel.objects.filter(id=taskID).delete()
    return redirect(request.META["HTTP_REFERER"])


def editTaskView(request, taskID):
    dict1 = {'todoID': taskID}
    return render(request, "todoApp/editTask.html", dict1)


def editTask(request, taskID):
    updateTask = request.POST['task']
    todo = TodoModel.objects.filter(id=taskID)[0]
    todo.task = updateTask
    todo.save()
    return redirect('todoHome')