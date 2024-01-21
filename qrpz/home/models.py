from django.db import models

# Create your models here.

class Puzzle(models.Model):
    Image = models.ImageField(upload_to="puzzle")
    Name = models.CharField(max_length=100)
    divID = models.IntegerField()
    


    def __str__(self):
        return self.Name