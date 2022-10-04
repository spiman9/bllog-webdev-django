from django import forms

from .models import Article
from django.forms import TextInput,Textarea

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 800px; margin-top: 10px; margin-bottom:10px;',
                'placeholder': 'Add the Blog Title here'
                }),
            'content' : forms.Textarea(attrs={
                'placeholder' : 'Write Your Blog Here',
                'rows' : 15,
                'cols' : 80,
                'style' : "margin-top:10px; margin-bottom:20px;vertical-align:top;padding:10px;"
                })
        }

    