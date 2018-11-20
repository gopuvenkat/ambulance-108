from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from django.contrib.auth.models import User, Group, AbstractUser
from django.contrib.auth import authenticate
from django.core import serializers
import json
from django.forms.models import model_to_dict
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hospital, Patient, Ambulance, Trip
from .serializers import HospitalSerializer, PatientSerializer, AmbulanceSerializer, TripSerializer
from common.utils import get_distance, assign_nearest_ambulance, get_nearest_hospital
# Create your views here.


class HospitalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hospitals to be viewed.
    """
    serializer_class = HospitalSerializer

    def get_queryset(self):
        queryset = Hospital.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset


@permission_classes((AllowAny, ))
class PatientCreate(APIView):
    """
    Creates the user.
    """
    def post(self, request, format='json'):
        serializer = PatientSerializer(data=request.data)
        if(serializer.is_valid()):
            user = serializer.save()
            if(user):
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((AllowAny, ))
def patient_login(request):
    name = request.data.get('name')
    dob = request.data.get('dob')
    contact_number = request.data.get('contact_number')
    if name is None or contact_number is None:
        return Response({'error': 'Please provide both name and DOB.'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        queryset = Patient.objects.all()
        patient = queryset.filter(name=name, contact_number=contact_number).first()
        if not patient:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_404_NOT_FOUND)
        user = authenticate(username=name, password=contact_number)
        if user is None:
            user = User.objects.create_user(username=name, password=contact_number)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)


@permission_classes((AllowAny, ))
class AmbulanceCreate(APIView):
    """
    Creates the ambulance.
    """
    def post(self, request, format='json'):
        serializer = AmbulanceSerializer(data=request.data)
        if(serializer.is_valid()):
            user = serializer.save()
            if(user):
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((AllowAny, ))
def ambulance_login(request):
    number_plate = request.data.get('number_plate')
    contact_number = request.data.get('contact_number')
    if number_plate is None or contact_number is None:
        return Response({'error': 'Please provide both number plate and contact number.'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        queryset = Ambulance.objects.all()
        ambulance = queryset.filter(number_plate=number_plate, contact_number=contact_number).first()
        if not ambulance:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_404_NOT_FOUND)
        user = authenticate(username=number_plate, password=contact_number)
        if user is None:
            user = User.objects.create_user(username=number_plate, password=contact_number)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class PatientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows patients to be viewed.
    """
    serializer_class = PatientSerializer

    def get_queryset(self):
        queryset = Patient.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset


class AmbulanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ambulances to be viewed.
    """
    serializer_class = AmbulanceSerializer

    def get_queryset(self):
        queryset = Ambulance.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset


class AmbulancePost(APIView):
    """
    put:
    API to complete trip.
    """
    def put(self, request):
        id = request.query_params.get('id', None)
        if(id):
            ambulance = get_object_or_404(Ambulance, id=id)
            ambulance.status = False
            ambulance.save()
            if(ambulance):
                result = {'id': ambulance.id, 'number_plate': ambulance.number_plate, 'latitude': ambulance.latitude, 'longitude': ambulance.longitude, 'contact_number': ambulance.contact_number, 'status': ambulance.status}
                return Response(result, status=status.HTTP_200_OK)
        return Response({'error': 'Please provide ID'}, status=status.HTTP_400_BAD_REQUEST)


class AmbulanceUpdate(APIView):
    """
    put:
    API to update location.
    """
    def put(self, request):
        id = request.query_params.get('id', None)
        if(id):
            ambulance = get_object_or_404(Ambulance, id=id)
            latitude = request.data.get('latitude', None)
            longitude = request.data.get('longitude', None)
            ambulance.latitude = latitude
            ambulance.longitude = longitude
            ambulance.save()
            result = {'id': ambulance.id, 'number_plate': ambulance.number_plate, 'latitude': ambulance.latitude, 'longitude': ambulance.longitude, 'contact_number': ambulance.contact_number, 'status': ambulance.status}
            return Response(result, status=status.HTTP_200_OK)
        return Response({'error': 'Please provide ID'}, status=status.HTTP_400_BAD_REQUEST)


class TripView(APIView):
    """
    get:
    API endpoint that allows trips to be viewed.

    post:
    API endpoint to create a trip.
    """
    def get(self, request):
        id = request.data.get('id', None)
        if(id):
            trip = get_object_or_404(Trip, id=id)
            resp = serializers.serialize("json", [trip.patient_id])
            patient = json.loads(resp)

            resp = serializers.serialize('json', [trip.ambulance_id])
            ambulance = json.loads(resp)

            resp = serializers.serialize('json', [trip.hospital_id])
            hospital = json.loads(resp)

            if(trip):
                result = {'id': trip.id, 'patient_id': patient, 'ambulance_id': ambulance, 'start_latitude': trip.start_latitude, 'start_longitude': trip.start_longitude, 'hospital': hospital}
                return Response(result, status=status.HTTP_200_OK)
        return Response({'error': 'Please provide ID'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        patient_id = request.data.get('patient_id', None)
        start_latitude = request.data.get('start_latitude', None)
        start_longitude = request.data.get('start_longitude', None)
        if(patient_id):
            patient = get_object_or_404(Patient, id=patient_id)
            if(start_latitude and start_longitude):
                pos = (float(start_latitude), float(start_longitude))
                ambulance = assign_nearest_ambulance(pos)
                hospital = get_nearest_hospital(pos)
                trip = Trip(patient_id=patient, ambulance_id=ambulance, start_latitude=start_latitude, start_longitude=start_longitude, hospital_id=hospital)
                trip.save()
                resp = serializers.serialize("json", [patient])
                patient = json.loads(resp)
                resp = serializers.serialize('json', [ambulance])
                ambulance = json.loads(resp)
                resp = serializers.serialize('json', [hospital])
                hospital = json.loads(resp)
                result = {'id': trip.id, 'patient_id': patient, 'ambulance_id': ambulance, 'start_latitude': trip.start_latitude, 'start_longitude': trip.start_longitude, 'hospital': hospital}
                return Response(result, status=status.HTTP_200_OK)
            return Response({'error': 'Please provide the latitude and longitude.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Please provide valid ID'}, status=status.HTTP_400_BAD_REQUEST)
