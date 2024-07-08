from django.db import models

# Create your models here.
class Todo(models.Model):
    Name= models.CharField(max_length=20)
    Task= models.CharField(max_length=100)