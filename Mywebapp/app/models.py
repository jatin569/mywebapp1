from django.db import models
class signup(models.Model):
    Name = models.CharField(max_length=40)
    Username = models.CharField(max_length=40)
    Email = models.CharField(max_length=40)
    Password = models.CharField(max_length=40)

class login(models.Model):
    Name = models.CharField(max_length=40)
    Password = models.CharField(max_length=40)
    Submit = models.CharField(max_length=40)