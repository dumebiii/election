from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.register, name='register'),
    path('thanks', views.thanks, name='thanks'),
    path('profile', views.profile, name='profile'),
    path('loginn', views.loginn, name='login'),
]