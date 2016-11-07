from django.db import models

# Create your models here.


class Crisis(models.Model):
    disaster = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    shapeType = models.CharField(max_length=10)
    description = models.CharField(max_length=300)
    time = models.CharField(max_length=50)
    region = models.CharField(max_length=10)
    location = models.CharField(max_length=300)
    severity = models.IntegerField()
    approved = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " " + self.disaster + " " + self.location

    def get_json(self):
        if Dispatch.objects.filter(crisis=self):
            # TODO
            dispatch = Dispatch.objects.get(crisis=self)
            return {
                'id': self.id,
                'disaster': self.disaster,
                'name': self.name,
                'type': self.shapeType,
                'description': self.description,
                'location': self.location,
                'region': self.region,
                'severity': self.severity,
                'time': self.time,
                'coordinates': [{'lat': coord.latitude, 'lng': coord.longitude} for coord in CrisisCoordinates.objects.filter(crisis=self)],
                'dispatch': {'agency': dispatch.agency, 'resource': dispatch.resource, 'contact': dispatch.contact, 'time': dispatch.time}}
        else:
            return {
                'id': self.id,
                'disaster': self.disaster,
                'name': self.name,
                'type': self.shapeType,
                'description': self.description,
                'location': self.location,
                'region': self.region,
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
        return str(self.inCrisis)


class Dispatch(models.Model):
    crisis = models.ForeignKey(Crisis, on_delete=models.CASCADE)
    agency = models.CharField(max_length=20)
    resource = models.CharField(max_length=300)
    contact = models.IntegerField()
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.crisis.name + " " + self.agency + " " + self.resource
