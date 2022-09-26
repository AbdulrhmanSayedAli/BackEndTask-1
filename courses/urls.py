from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Courses.as_view()),
    path('<int:id>', views.SingleCourse.as_view()),
]
