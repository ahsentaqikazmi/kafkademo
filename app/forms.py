from django import forms

class SensorForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    url = forms.CharField(label='url', max_length=50)
    numofparams = forms.IntegerField(required=False)
    nameofparams = forms.CharField(label='nameofparams', max_length=100)
    endpoints = forms.CharField(label='endpoints', max_length=100)