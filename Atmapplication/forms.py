from django import forms
from atm_interface.models import MinLengthValidator


class CardNumberForm(forms.Form):
    number = forms.CharField(max_length=19, validators=[MinLengthValidator(19)],)
