from django.db import models

class Character(models.Model):
    name =models.CharField(max_length= 20)
    feature = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
