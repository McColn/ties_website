from django.db import models

# Create your models here.
class Message(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()