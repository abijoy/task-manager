from django.forms.models import BaseModelForm
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task, Photo
from .forms import TaskForm
# Create your views here.
def index(request):
    return HttpResponse(f'Hello - {request.user}. This your Tasks home')


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    paginate_by = 5

    def get_queryset(self):
        # return Task.objects.filter(user=self.request.user)
        qs = filter(self.request)
        return qs
    

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
    # fields = ['title', 'description', 'due_date', 'priority']

    form_class = TaskForm


    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        photos = request.FILES.getlist('photo')
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            for p in photos:
                Photo.objects.create(task=f, photo=p)
            
            return HttpResponseRedirect('/tasks/all/')
        else:
            self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
    
    success_url = reverse_lazy('tasks:tasks-all')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    # fields = ['title', 'description', 'due_date', 'priority', 'is_completed']
    form_class = TaskForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["prev_photos"] = self.object.photos.all()
        print(context['prev_photos'])
        return context

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


def is_valid_queryparam(param):
    return param != '' and param is not None

def filter(request):
    qs = Task.objects.filter(user=request.user)
    title = request.GET.get('title')
    creation_date = request.GET.get('creation_date')
    due_date = request.GET.get('due_date')
    priority = request.GET.get('priority')
    is_completed = request.GET.get('is_completed')


    if is_valid_queryparam(title):
        qs = qs.filter(title__icontains=title)

    if is_valid_queryparam(due_date):
        qs = qs.filter(due_date=due_date)

    if is_valid_queryparam(creation_date):
        qs = qs.filter(created_at__date=creation_date)

    if is_valid_queryparam(priority):
        qs = qs.filter(priority=priority)

    if is_completed == 'on':
        qs = qs.filter(is_completed=True)
    
    return qs

