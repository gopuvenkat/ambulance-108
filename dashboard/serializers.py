from django.contrib.auth.models import User, Group
from .models import Hospital, Patient, Ambulance, Trip
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'patient_id', 'ambulance_id', 'start_latitude', 'start_longitude', 'hospital_id')


class HospitalSerializer(serializers.ModelSerializer):

    trips = TripSerializer(many=True, read_only=True)

    class Meta:
        model = Hospital
        fields = ('id', 'name', 'latitude', 'longitude', 'trips')


class PatientSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, validators=[UniqueValidator(queryset=Patient.objects.all())])
    dob = serializers.DateField(required=False)
    contact_number = serializers.CharField(validators=[UniqueValidator(queryset=Patient.objects.all())])

    trips = TripSerializer(many=True, read_only=True)

    def create_user(self, validated_data):
        patient = Patient.objects.create_user(validated_data['name'], validated_data['dob'], validated_data['contact_number'])
        return patient

    class Meta:
        model = Patient
        fields = ('id', 'name', 'dob', 'contact_number', 'trips')


class AmbulanceSerializer(serializers.ModelSerializer):

    trips = TripSerializer(many=True, read_only=True)

    class Meta:
        model = Ambulance
        fields = ('id', 'number_plate', 'latitude', 'longitude', 'contact_number', 'status', 'trips')
