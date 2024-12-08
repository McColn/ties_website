from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True,blank=True, default="null")
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    role = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.email


class Message(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True, blank=True)
    phoneNumber = models.CharField(max_length=15, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.fullName

class Project(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    timeframe = models.CharField(max_length=200)
    Commodities = models.CharField(max_length=200)
    status = models.CharField(max_length=200, default='ongoing')
    body = models.TextField()
    image = models.ImageField()
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ProjectImages(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.image

class Blog(models.Model):
    title = models.CharField(max_length=200)
    uploader = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    body = models.TextField()
    uploaded = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    image = models.ImageField()

    def __str__(self):
        return self.title



class Service(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField()
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ServicePoint(models.Model):
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    point = models.CharField(max_length=2000)

    def __str__(self):
        return f"{self.point} - {self.service.title}"

class Team(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    profile = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name
    
class GoldPrice(models.Model):
    usd = models.FloatField()
    usdtoz = models.FloatField()
    perGramWordTzs = models.FloatField(null=True, blank=True)
    perGramWordUsd = models.FloatField(null=True, blank=True)
    perGramLocalTzs = models.FloatField(null=True, blank=True)
    perGramLocalUsd = models.FloatField(null=True, blank=True)
    perKgWordTzs = models.FloatField(null=True, blank=True)
    perKgWordUsd = models.FloatField(null=True, blank=True)
    perKgLocalTzs = models.FloatField(null=True, blank=True)
    perKgLocalUsd = models.FloatField(null=True, blank=True)
    uploadedDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.usd)

    def save(self, *args, **kwargs):
        self.perGramWordTzs = (self.usd * self.usdtoz) / 31.10349947
        self.perGramWordUsd = self.usdtoz
        self.perGramLocalTzs = self.perGramWordTzs * 0.9
        self.perGramLocalUsd = self.perGramWordUsd * 0.9
        self.perKgWordTzs = self.perGramWordTzs * 1000
        self.perKgWordUsd = self.perGramWordUsd * 1000
        self.perKgLocalTzs = self.perGramLocalTzs * 1000
        self.perKgLocalUsd = self.perGramLocalUsd * 1000
        super().save(*args, **kwargs)