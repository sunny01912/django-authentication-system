"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from myapp import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='myapp/home.html'),name='home'),
    path('dashboard/',TemplateView.as_view(template_name='myapp/dash.html'),name='dashboard'),
    path('login/',v.customLoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='myapp/logout.html'),name='logout'),
    path('passchange/',v.customPasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='myapp/passdone.html'),name='password_change_done'),
    path('password_reset/',v.customPasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    

    
    

]
