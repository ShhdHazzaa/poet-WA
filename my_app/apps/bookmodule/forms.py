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
                'id': 'poem_title_id',
                'aria-label': 'عنوان القصيدة'
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
                'id': 'poem_content_id',
                'aria-label': 'محتوى القصيدة'
            }
        )
    )

    poet = forms.ModelChoiceField(
        queryset=Poet.objects.all(),
        required=True,
        label='الشاعر',
        widget=forms.Select(
            attrs={
                'class': 'mycssclass',
                'id': 'poet_id',
                'aria-label': 'اختر شاعر'
            }
        )
    )
