from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.add_task,name="add_task"),
     path('edit/<int:id>/', views.editTask, name="editTask"),
    path('delete/<int:id>/', views.deleteTask, name="deleteTask"),
    
]
