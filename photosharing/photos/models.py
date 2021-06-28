from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
      return self.name

class Photo(models.Model):
    description = models.CharField(max_length=500)

    def __str__(self):
      return self.name