from django.db import models

# Create your models here.

class Note(models.Model):
    title=models.CharField(max_length=300)
    content=models.TextField(max_length=2000)

    def __str__(self):
        return self.title[0:30]