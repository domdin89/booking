from django.db import models
from services.models import Service
from structures.models import Structure


# Create your models here.
class Reservation(models.Model):
    #profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.service, self.structure, str(self.date)