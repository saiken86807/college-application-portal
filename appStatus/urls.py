from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('apply', views.apply, name="apply"),
    path('applications', views.applications, name="applications"),
    path('applicant/<str:pk_test>/', views.applicant, name="applicants"),
]
