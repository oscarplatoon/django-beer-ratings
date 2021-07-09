from django.forms import ModelForm
from .models import Beer, Review


class BeerForm(ModelForm):
    class Meta:
        model = Beer
        fields = ['name']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['stars', 'title', 'content']
        exclude = ['beer', 'author']
