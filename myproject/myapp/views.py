from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
from .forms import LoginForm,PasschangeForm

from django.contrib.auth import views as auth_views


class customLoginView(auth_views.LoginView):
    template_name='myapp/login.html'
    form_class=LoginForm
    redirect_authenticated_user=True

class customPasswordChangeView(auth_views.PasswordChangeView):
    template_name='myapp/pass.html'
    form_class=PasschangeForm

class customPasswordResetView(auth_views.PasswordResetView):
    from_email='sunnyraj01912@gmail.com'


