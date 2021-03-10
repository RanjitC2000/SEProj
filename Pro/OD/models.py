from django.db import models

# Create your models here.
class ODList(models.Model):
    SNo = models.IntegerField()
    RollNo = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    ClassAdvisor = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "ODs"

    def __str__(self):
        return self.Name

