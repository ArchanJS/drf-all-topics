from django.contrib import admin
from .models import Person,Post

# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display=['id','name','email']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','content','postedby']