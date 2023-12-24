from django.urls import path 

from .views import TaskList, TaskDetail

urlpatterns = [
    path('', TaskList.as_view(), name="post-list"),
    path('<int:pk>/', TaskDetail.as_view(), name='task-detail')
]