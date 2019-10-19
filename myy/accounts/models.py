from django.db import models

# Create your models here.
class Register(models.Model):
    Username=models.CharField(max_length=100)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    Email=models.EmailField()

    def __str__(self):
        return self.Username


class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()