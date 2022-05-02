from django.db import models

# Create your models here.

class Comment(models.Model):
    title=models.CharField(max_length=300)
    content=models.CharField(max_length=3000)

    def __str__(self):
        return self.title

