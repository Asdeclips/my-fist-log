from django import forms

from .models import Game, Card

class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('name', 'big_picture', 'palette',)


class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ('title', 'is_bright', 'text',)