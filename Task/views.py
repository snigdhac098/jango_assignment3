from django.shortcuts import render,redirect
from . import forms
from . import models

def add_task(request):
    if request.method == "POST":
         display_form=forms.TaskForm(request.POST)
         if display_form.is_valid():
              display_form.save()
              return redirect('add_task')
    else:
          display_form=forms.TaskForm()
    return render (request,'task.html',{'form':display_form}) 


def editTask(request, id):
    task = models.Task.objects.get(pk=id)
    form = forms.TaskForm(instance=task)
    if request.method == 'POST':
        form = forms.TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("homePage")

    return render(request, 'task.html', {'form': form})


def deleteTask(request, id):
    task = models.Task.objects.get(pk=id)
    task.delete()
    return redirect("homePage")