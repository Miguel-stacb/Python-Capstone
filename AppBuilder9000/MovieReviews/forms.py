# MovieReviews/forms.py

from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'rating', 'release_date']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'release_date': forms.SelectDateWidget(years=range(1900, 2100)),
        }
