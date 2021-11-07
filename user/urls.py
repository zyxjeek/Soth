from django.urls import path
from django.contrib.auth.views import auth_login

from . import views


urlpatterns = [
    path("signup/", views.signup, name="signup")
]
