from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from tasks.models import Task

from .serializers import TaskSerializer
from .permissions import IsOwnerOnly

class TaskList(generics.ListCreateAPIView):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerOnly]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)




# Create your views here.