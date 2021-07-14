from django import forms
from .models import Beer, Review

class BeerForm(forms.ModelForm):
    class Meta:
        model = Beer
        fields = {'beer_brewer', 'beer_name', 'beer_type'}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = {'review',}