from django.db import models

class Car(models.Model):
    id = models.AutoField(primary_key=True) #auto increment
    model=models.CharField(max_length=200) #string
    brand= models.CharField(max_length=200) #marca
    factory_year=models.IntegerField(blank=True,null=True)
    model_year=models.IntegerField(blank=True,null=True)
    value=models.FloatField(blank=True,null=True) # float
    
    