from django.shortcuts import render

from django.shortcuts import render
from Task.models import Task

def show_task(request):
    # data=Task.objects.all()
    tasks = Task.objects.prefetch_related('Categories').all()
    # for i in tasks:
    #     print(i.Categories.all)
    #     for j in i.Categories.object.all:
    #         print("line 12 ",j.Category_name)
    return render(request,'show_task.html',{'data' : tasks})


def home_page(request):
    return render(request,'homepage.html')
