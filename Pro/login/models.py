from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Students"

    def __str__(self):
        return self.username

class Faculty(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = "Faculties"

    def __str__(self):
        return self.username
