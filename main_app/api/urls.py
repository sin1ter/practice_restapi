from django.urls import path

from main_app.api.views import *

urlpatterns = [
    path('todolist/', TodoListCreateView.as_view(), name='todo-list'),
    path('todolist/<int:pk>/', TodoListDetailView.as_view(), name='todo-detail'),
    path('todolist/completed/', CompletedTaskView.as_view(), name='todo-complete'),
    path('todolist/not-completed/', NotCompletedTaskView.as_view(), name='todo-notcomplete'),
    
]
