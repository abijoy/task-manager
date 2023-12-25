from django.urls import path, include
from . import views

app_name = 'tasks'

urlpatterns = [
    # path('', views.index, name="index"),
    path('', views.TaskListView.as_view(), name='tasks-all'),
    path('all/', views.TaskListView.as_view(), name='tasks-all'),
    path('task/create/', views.TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('task/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),
]
