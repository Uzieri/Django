from django.db import models
class Vehicles(models.Model):

    Name = models.CharField(max_length = 200)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.Name} produced in {self.year}'