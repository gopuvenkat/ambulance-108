from django.contrib import admin
from .models import Hospital, Patient, Ambulance, Trip

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Patient)
admin.site.register(Ambulance)
admin.site.register(Trip)
