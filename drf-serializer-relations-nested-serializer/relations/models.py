from django.db import models

# Create your models here.

# Person
class Person(models.Model):
    name=models.CharField(max_length=300)
    email=models.EmailField(max_length=300)

    def __str__(self):
        return self.name

# Post
class Post(models.Model):
    title=models.CharField(max_length=300)
    content=models.TextField(max_length=3000)
    postedby=models.ForeignKey(Person,on_delete=models.CASCADE,related_name='person')

    def __str__(self):
        return self.title