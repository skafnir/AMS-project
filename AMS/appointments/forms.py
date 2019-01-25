from django import forms
from django.contrib.auth.models import User

from main.models import Service


class AppointmentRequestForm(forms.Form):
    services = forms.ModelMultipleChoiceField(queryset=Service.objects.all(), label='services',
                                              widget=forms.CheckboxSelectMultiple)
    date_from = forms.CharField(label='Most suitable date')
    extra_info = forms.CharField(widget=forms.Textarea, required=False)
