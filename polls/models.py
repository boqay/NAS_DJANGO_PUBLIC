from django.db import models
from django.utils import timezone

class User(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    pwd = models.CharField(max_length=500)
    email = models.EmailField()
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)