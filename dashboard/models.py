from django.db import models

# Create your models here.

class Hospital(models.Model):

    name = models.CharField(max_length=255, null=False)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return "{} {} {}".format(self.name, self.latitude, self.longitude)


class Patient(models.Model):

    name = models.CharField(max_length=255, null=False)
    dob = models.DateField()
    contact_number = models.CharField(max_length=10)

    def __str__(self):
        return "{} {} {}".format(self.name, self.dob, self.contact_number)


class Ambulance(models.Model):

    number_plate = models.CharField(max_length=15)
    latitude = models.FloatField()
    longitude = models.FloatField()
    contact_number = models.CharField(max_length=10)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "{} {} {} {}".format(self.number_plate, self.latitude, self.longitude, self.contact_number)


class Trip(models.Model):

    patient_id = models.ForeignKey(Patient, models.SET_NULL, null=True)
    ambulance_id = models.ForeignKey(Ambulance, models.SET_NULL, null=True)
    start_latitude = models.FloatField(null=False)
    start_longitude = models.FloatField(null=False)
    hospital_id = models.ForeignKey(Hospital, models.SET_NULL, null=True)

    def __str__(self):
        return "{} {} {} {} {}".format(self.patient_id, self.ambulance_id, self.start_latitude, self.start_longitude, self.hospital_id)
