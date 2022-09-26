from django.db import models


class User (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(
        min_length=8, max_length=20)
    birthDate = models.DateField()
