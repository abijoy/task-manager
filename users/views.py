from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def dashboard(request):
    return render(request, 'users/dashboard.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tasks:index')
        return render(request, 'users/register.html', {'form': form})
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})