from django import forms
from .models import Poem, Poet

class PoemForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ['title', 'content', 'poet']

    title = forms.CharField(
        max_length=100,
        required=True,
        label='عنوان القصيدة',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ادخل عنوان القصيدة هنا',
                'class': 'mycssclass',
                'id': 'myid',
            }
        )
    )

    content = forms.CharField(
        required=True,
        label='محتوى القصيدة',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'ادخل محتوى القصيدة هنا',
                'class': 'mycssclass',
                'id': 'myid',
            }
        )
    )

    poet = forms.ModelChoiceField(
        queryset=Poet.objects.all(),
        required=True,
        label='الشاعر'
    )


class PoetForm(forms.ModelForm):
    class Meta:
        model = Poet
        fields = ['name', 'description']

    name = forms.CharField(
        max_length=100,
        required=True,
        label='اسم الشاعر'
    )

    description = forms.CharField(
        required=True,
        label='نبذة عن الشاعر',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'ادخل نبذة عن الشاعر هنا',
                'class': 'mycssclass',
                'id': 'myid',
            }
        )
    )
