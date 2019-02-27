from django.contrib.auth.models import User
from django.forms import ModelForm


class ProfileEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

