from django.contrib import admin

# Register your models here.

from .models import Applicant, Status

admin.site.register(Applicant)
admin.site.register(Status)
