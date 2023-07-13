from django import forms
from .models import *


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['clients','rating', 'description']
        widgets = {
            'clients': forms.TextInput(attrs={'class':'text=input'}),
            'rating': forms.TextInput(attrs={'class':'text=input'}),
            'description':forms.Textarea(attrs={'cols':60, 'rows': 10})
        }
