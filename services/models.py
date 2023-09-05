from django.db import models
from structures.models import Structure



# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    data_da = models.DateField(blank=True, null=True)
    data_a = models.DateField(blank=True, null=True)
    orario_da = models.TimeField(blank=True, null=True)
    orario_a = models.TimeField(blank=True, null=True)


    def __str__(self):
        return self.name