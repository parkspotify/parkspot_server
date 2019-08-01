from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import PS2UserCreationForm, PS2UserChangeForm
from .models import PS2User

# Register your models here


class PS2UserAdmin(UserAdmin):
    model = PS2User
    add_form = PS2UserCreationForm
    form = PS2UserChangeForm

admin.site.register(PS2User, PS2UserAdmin)