from django.db import models

# Create your models here.

class Destination(models.Model):
    Name=models.CharField(max_length=100)
    Desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    Image=models.ImageField(upload_to='pics')