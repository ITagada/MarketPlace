from .models import articles
from django.forms import ModelForm, TextInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = articles
        fields = ['title', 'price', 'description', 'remains']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование товара'
            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            'remains': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Остаток'
            })
        }