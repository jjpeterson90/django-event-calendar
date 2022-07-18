from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('account/', views.index, name="account"),
    path('account/signup/', views.sign_up, name="signup"),
    path('account/login/', LoginView.as_view(), name="login"),
    path('account/logout', LogoutView.as_view(), name="logout"),
    # path('account/who-am-i', views.who_am_i, name="whoami"),
]