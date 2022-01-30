from django import forms


class Calculate_age(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
