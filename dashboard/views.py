from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User, Group, AbstractUser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hospital, Patient, Ambulance, Trip
from .serializers import HospitalSerializer, PatientSerializer, AmbulanceSerializer, TripSerializer

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
def login(request):
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


class TripViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows trips to be viewed.
    """
    serializer_class = TripSerializer

    def get_queryset(self):
        queryset = Trip.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset
