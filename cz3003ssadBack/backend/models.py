from django.db import models

# Create your models here.


class Crisis(models.Model):
    disaster = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    shapeType = models.CharField(max_length=10)
    description = models.CharField(max_length=300)
    time = models.CharField(max_length=50)
    location = models.CharField(max_length=300)
    severity = models.IntegerField()
    approved = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " " + self.disaster + " " + self.location

    def get_json(self):
        return {
            'id': self.id,
            'disaster': self.disaster,
            'name': self.name,
            'type': self.shapeType,
            'description': self.description,
            'location': self.location,
            'severity': self.severity,
            'time': self.time,
            'coordinates': [{'lat': coord.latitude, 'lng': coord.longitude} for coord in CrisisCoordinates.objects.filter(crisis=self)]}


class CrisisCoordinates(models.Model):
    crisis = models.ForeignKey(Crisis, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.crisis.name + " lat:" + str(self.latitude) + " lng:" + str(self.longitude)


class CrisisMode(models.Model):
    inCrisis = models.BooleanField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.inCrisis


class Dispatch(models.Model):
    crisis = models.ForeignKey(Crisis, on_delete=models.CASCADE)
    dispatcher = models.CharField(max_length=20)

    def __str__(self):
        return self.crisis.name + " " + self.dispatcher
