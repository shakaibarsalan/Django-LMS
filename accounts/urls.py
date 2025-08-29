from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Account_app, name='Account_app'),
]
