from django.urls import path
from django.conf.urls import include, url
from .views import HospitalViewSet, PatientCreate, login, PatientViewSet, AmbulanceViewSet, TripView

urlpatterns = [
    path(r'hospital/', HospitalViewSet.as_view({'get': 'list'}), name='hospital-all'),
    path(r'patient/', PatientViewSet.as_view({'get': 'list'}), name='patient-all'),
    path(r'ambulance/', AmbulanceViewSet.as_view({'get': 'list'}), name='ambulance-all'),
    path(r'trip/', TripView.as_view(), name='trip-all'),
    url(r'signup/', PatientCreate.as_view(), name='patient-signup'),
    url(r'signin/', login, name='patient-login')
]
