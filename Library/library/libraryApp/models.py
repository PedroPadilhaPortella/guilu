from django.db import models

# Create your models here.
class Lib(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)