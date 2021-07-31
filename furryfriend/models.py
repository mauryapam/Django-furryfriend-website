from django.db import models

# Create your models here.
class Pets(models.Model):
    
    img = models.ImageField(upload_to='pics') 
    category = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    desc = models.TextField()
    owner = models.IntegerField()