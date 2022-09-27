from django.db import models
from datetime import date


class User (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    birthDate = models.DateField()

    @property
    def age(self):
        today = date.today()
        born = self.birthDate
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    @property
    def name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.name+"("+str(self.pk)+")"

    class Meta:
        db_table = "myUsers"
        ordering = ['first_name']
