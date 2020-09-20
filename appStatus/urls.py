from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('user', views.userPage, name='user-page'),
    path('apply', views.apply, name="apply"),
    path('applications', views.applications, name="applications"),
    path('application_review/<str:pk>/',
         views.applicationReview, name='application_review')
]
