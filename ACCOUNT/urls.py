from django.contrib import admin
from django.urls import path, include
from ACCOUNT import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
