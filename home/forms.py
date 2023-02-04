from django import forms
from .models import Note


class AddNoteFrom(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title','body')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'تایتل'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'متن'
            })
        }

