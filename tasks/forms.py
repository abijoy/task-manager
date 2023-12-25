from django import forms
from .models import Task, Photo


class TaskForm(forms.ModelForm):
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'is_completed', 'photo']
        widgets = {
            'due_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            )
        }
		

class PhotoForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = Photo
        fields = ('photo', )


# PhotoFormSet = forms.modelformset_factory(Photo,
#                                         form=PhotoForm, extra=4)