from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Puzzle(models.Model):
    Image = models.ImageField(upload_to="puzzle")
    Name = models.CharField(max_length=100)
    def __str__(self):
        return self.Name
    

class Scan(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    code = models.CharField(max_length=50)