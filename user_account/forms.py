from django import forms
from django.forms.widgets import Textarea
from .models import UserAccount


class UserAccountForm(forms.Form):
    user = forms.ModelChoiceField(queryset=UserAccount.objects.all(), label='Пользователь')
    summa = forms.DecimalField(max_digits=11, decimal_places=2, label='Сумма')
    to_inns = forms.CharField(max_length=512, widget=Textarea, label='на ИНН')
