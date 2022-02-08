from django import forms


class CalculateAge(forms.Form):
    name = forms.CharField(max_length=50)
    date_birth = forms.IntegerField()


class CalculateCurrency(forms.Form):
    OPTIONS = [
        ("DOL", "Dollar"),
        ("EUR", "EUR"),
        ]

    currency = forms.ChoiceField(
            choices=OPTIONS,
            label='Office',
        )
    amount = forms.IntegerField()


class CalculateWeather(forms.Form):
    city = forms.CharField(max_length=50)
