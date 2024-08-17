from django import forms

class Contact(forms.Form):
    name = forms.CharField(max_length=250)
    email = forms.CharField(max_length=250)
    message = forms.CharField(widget=forms.Textarea())