from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import PS2User

""" 
    Various forms in Django interact with the user especially around creating and changing users. 
    We’ll update both the default UserCreationForm and UserChangeForm to point to our new PS2User model.
"""


class PS2UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = PS2User
        fields = ('email', 'password1', 'password2')


class PS2UserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = PS2User
        fields = UserChangeForm.Meta.fields


class PS2UserSignIn(AuthenticationForm):

    class Meta(UserCreationForm):
        model = PS2User
        fields = ('email', 'password1', 'password2')