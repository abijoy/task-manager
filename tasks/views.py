from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
# Create your views here.
def index(request):
    return HttpResponse(f'Hello - {request.user}. This your Tasks home')


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    

from django.core.exceptions import PermissionDenied
class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'

    def get_object(self, queryset=None):
        obj = get_object_or_404(self.model, pk=self.kwargs.get('pk'))
        if obj.user != self.request.user:
            raise PermissionDenied("You cannot view this task.")
        return obj 
    

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'priority']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
    
    success_url = reverse_lazy('tasks:tasks-all')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'priority', 'is_completed']

    def get_object(self, queryset=None):
        obj = get_object_or_404(self.model, pk=self.kwargs.get('pk'))
        if obj.user != self.request.user:
            raise PermissionDenied("You cannot edit this Task.")
        return obj
    
    success_url = reverse_lazy('tasks:tasks-all')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'


    def get_object(self, queryset=None):
        obj = get_object_or_404(self.model, pk=self.kwargs.get('pk'))
        if obj.user != self.request.user:
            raise PermissionDenied("You cannot delete this Task.")
        return obj
    
    success_url = reverse_lazy('tasks:tasks-all')


# class TaskCRUDView(View):
#     def get(self, request, id):
#         task = Task.objects.get(id=id)
#         return render(request, 'tasks/task.html', {'task': task})

#     # def post(self, request):
#     #     # Create an object
#     #     item = Task.objects.create(
#     #         title=request.POST['title'], 
#     #         description=request.POST['description']
#     #     )
#     #     return redirect('Task-list')

#     # def put(self, request, pk):
#     #     # Update an object
#     #     item = Task.objects.get(pk=pk)
#     #     item.title = request.POST['title']
#     #     item.description = request.POST['description']
#     #     item.save()
#     #     return redirect('Task-list')

#     # def delete(self, request, pk):
#     #     # Delete an object
#     #     item = Task.objects.get(pk=pk)
#     #     item.delete()
#     #     return redirect('Task-list')
