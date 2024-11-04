from django import forms
from .models import Music

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['date', 'music_name']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }