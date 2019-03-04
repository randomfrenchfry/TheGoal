from django import forms

class LogInForm(forms.Form):
    userName = forms.CharField(label='User Name', max_length=70)
    password = forms.CharField(label='Password', max_length=70)
