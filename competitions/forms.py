from django import forms
from django.contrib.auth.models import User
from competitions.models import Challenge


class SolveForm(forms.Form):
    challenge = forms.ModelChoiceField(queryset=Challenge.objects.all(), widget=forms.HiddenInput())


class AdminSolveForm(SolveForm):
    user = forms.ModelChoiceField(label='For user', queryset=User.objects.all())