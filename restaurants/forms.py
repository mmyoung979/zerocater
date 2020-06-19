# Django Imports
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

# Python Imports
from datetime import datetime


# Enter search term for analysis.py
class ValidationForm(forms.Form):
    vendor_id = forms.IntegerField(
                    validators=[
                        MinValueValidator(1),
                        MaxValueValidator(2),
                    ],
                    widget=forms.TextInput(
                        attrs={
                            'placeholder': '1 or 2 only'
                        }
                    )
                )

    date = forms.DateTimeField(
                    initial=datetime.strptime('2017-01-01 14:30:00', '%Y-%m-%d %H:%M:%S'),
                    input_formats=['%Y-%m-%d %H:%M:%S']
                )
