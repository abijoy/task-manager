from django.urls import path, include
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name="index"),
]