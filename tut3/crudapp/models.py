from django.db import models

# Create your models here.
class DetailsModel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    
