from .models import lesson, lesson_e
from django.forms import ModelForm, TextInput


class lessonForm(ModelForm):
    class Meta:
        model = lesson
        fields = ['classroom']

        widgets ={
            'classroom': TextInput(attrs={
                'placeholder': 'Порожньо'
            })
        }

class lessoneForm(ModelForm):
    class Meta:
        model = lesson_e
        fields = ['classroom']

        widgets ={
            'classroom': TextInput(attrs={
                'placeholder': 'Порожньо'
            })
        }
