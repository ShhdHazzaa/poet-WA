from django import forms
from .models import Poem, Poet

class PoemForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ['title', 'body', 'poet']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'أدخل عنوان القصيدة'}),
            'body': forms.Textarea(attrs={'placeholder': 'أدخل محتوى القصيدة'}),
        }
class PoetForm(forms.ModelForm):
    class Meta:
        model = Poet
        fields = ['name', 'bio']
