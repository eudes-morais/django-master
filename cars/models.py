from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    # Exibindo a lista da classe em ordem alfabética
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Car(models.Model):
    # Esta será a ordem de apresentação do MODELFORM
    id = models.AutoField(primary_key=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    model = models.CharField(max_length=200)
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.model} - {self.plate} - {self.brand_id}'

class CarInventory(models.Model):
    # Não foi colocado o ID, mas o DJANGO já cria automaticamente o campo PRIMARY KEY
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Subeescrevendo a classe META do model CARINVENTORY
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'