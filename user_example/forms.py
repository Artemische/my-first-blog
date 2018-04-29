from django import forms
from.models import *

class InformForm(forms.ModelForm):
    task = forms.IntegerField(widget=forms.HiddenInput)
    class Meta:
        model = Inform
        exclude = ['']
