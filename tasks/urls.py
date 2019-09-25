from django.urls import path

from . import views

urlpatterns = [
    path('helloworld/', views.helloWorld),
    path('', views.taskList, name='task-list'),
    path('newtask/', views.newTask, name='new-task'),
    path('task/<int:id>', views.taskView, name='edit-task'),
    path('edit/<int:id>', views.editTask, name='task-view'),
    path('delete/<int:id>', views.deleteTask, name='delete-task'),
    path('yourname/<str:name>', views.yourName, name='your-name'),
]
