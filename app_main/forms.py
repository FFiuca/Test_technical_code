from django import forms

class FormValidation(forms.Form):
    number = forms.IntegerField(required=True)
