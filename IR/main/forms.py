from django import forms
from django.forms import ModelForm

class SearchForm(forms.Form):
    query = forms.CharField()
        