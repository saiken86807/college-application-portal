from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Application


class ApplicantForm(ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'phone', 'email', 'school', 'major', 'GPA']
        exclude = ['user']


class DecisionForm(ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'school', 'major', 'GPA', 'status']


class SearchCriteriaForm(ModelForm):
    class Meta:
        model = Application
        fields = ['major', 'status']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
