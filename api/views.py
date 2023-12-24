from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from tasks.models import Task

from .serializers import TaskSerializer


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated]


# Create your views here.
