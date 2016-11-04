from django.db import models

# Create your models here.

class Crisis(models.Model):
    disaster = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    shapeType = models.CharField(max_length=10)
    description = models.CharField(max_length=300)
    time = models.DateTimeField(auto_now_add=True)
    location = CharField(max_length=300)
    severity = models.IntegerField()

    def __str__(self):
       return self.name

class CrisisCoordinates(models.Model):
    crisis = models.ForeignKey(Crisis, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
       return self.crisis.name

class CrisisMode(models.Model):
    inCrisis = models.BooleanField()

    def __str__(self):
        return self.inCrisis
