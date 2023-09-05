from django.db import models
from city.models import City

class Structure(models.Model):
    logo = models.CharField(max_length=250, blank=True, null=True)
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Create your models here.
