from django.db import models

class Brand(models.Model):
    id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True) #auto increment
    model=models.CharField(max_length=200) #string
    brand= models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') #marca
    factory_year=models.IntegerField(blank=True,null=True)
    model_year=models.IntegerField(blank=True,null=True)
    value=models.FloatField(blank=True,null=True) # float
    photo=models.ImageField(upload_to='cars/',blank=True,null=True)
    bio= models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.model
    
class CarInventory(models.Model):
    cars_count= models.IntegerField()
    cars_value=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at'] # ordena de forma decrescente
    
    # cada instancia vai retornar oq está dentro do dunder 
    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'

