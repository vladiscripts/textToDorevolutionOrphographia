from django import forms


class InputForm(forms.Form):
    do = forms.CharField(widget=forms.Textarea(attrs=dict(cols="130", rows="15", placeholder='Search')))


class OutputForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs=dict(cols="130", rows="15", placeholder='Out')))
