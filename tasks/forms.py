from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['title', 'description', 'due_date', 'priority', 'is_completed']
		widgets = {
            'due_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            )
        }