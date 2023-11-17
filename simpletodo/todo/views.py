from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'todo/task_form.html', {'form': form})

def task_update(request, id):
    task = get_object_or_404(Task, id=id)
    form = TaskForm(request.Post or None, instance=task)
    if form.is_valid():
       form.save()
       return redirect('task_list')
    return render(request, 'todo/task_form.html', {'form': form, 'task': task})

def task_delete(request, id):
     task = get_object_or_404(Task, id=id)
     if request.method == 'POST':
         task.delete()
         return redirect('task_list')
     return render(request, 'todo/task_confirm_delete.html', {'object': task})
 