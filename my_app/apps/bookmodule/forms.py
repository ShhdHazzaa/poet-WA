from django import forms
from .models import Poet, Poem

class PoetForm(forms.ModelForm):
    class Meta:
        model = Poet
        fields = ['name', 'bio']
        labels = {
            'name': 'Poet Name',
            'bio': 'Biography',
        }
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }

class PoemForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ['title', 'content', 'poet']
        labels = {
            'title': 'Title',
            'content': 'Content',
            'poet': 'Poet',
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }
 
 
