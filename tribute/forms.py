from django import forms

from .models import Card

class PostForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ('title', 'text',)