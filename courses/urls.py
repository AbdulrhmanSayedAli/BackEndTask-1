from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Courses.as_view()),
    path('<str:id>', views.SingleCourse.as_view()),
]
