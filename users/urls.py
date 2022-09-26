from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Users.as_view()),
    path('<str:id>', views.SingleUser.as_view()),
]
