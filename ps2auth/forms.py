from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model

from .models import PS2User

""" 
    Various forms in Django interact with the user especially around creating and changing users. 
    We’ll update both the default UserCreationForm and UserChangeForm to point to our new PS2User model.
"""


class PS2UserCreationForm(UserCreationForm):
    mail = forms.CharField(max_length=128, required=True)
    password = forms.CharField(max_length=128, required=True)

    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('email', 'password')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(user.password)  # set password properly before commit
        if commit:
            user.save()
        return user


class PS2UserChangeForm(UserChangeForm):
    mail = forms.CharField(max_length=128, required=True)
    password = forms.CharField(max_length=128, required=True)

    class Meta(UserChangeForm):
        model = PS2User
        fields = UserChangeForm.Meta.fields


class PS2UserSignIn(AuthenticationForm):
    mail = forms.CharField(max_length=128, required=True)
    password = forms.CharField(max_length=128, required=True)

    class Meta(UserCreationForm):
        model = PS2User
        fields = ('email', 'password')