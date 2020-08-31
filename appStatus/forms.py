from django.forms import ModelForm
from .models import Applicant, Status


class ApplicantForm(ModelForm):
    class Meta:
        model = Applicant
        fields = ['name', 'school', 'major', 'GPA']


class DecisionForm(ModelForm):
    class Meta:
        model = Status
        fields = '__all__'
