from django.db import models
from django.core.exceptions import ValidationError


class Course (models.Model):
    title = models.CharField(max_length=100)
    subTitle = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=500)
    price = models.FloatField()
