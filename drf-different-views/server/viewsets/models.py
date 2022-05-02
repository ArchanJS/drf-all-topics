from django.db import models

# Create your models here.

class Teacher(models.Model):
    name=models.CharField(max_length=300)
    subject=models.CharField(max_length=300)

    def __str__(self):
        return self.name