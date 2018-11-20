from django.urls import path
from django.conf.urls import include, url
from .views import HospitalViewSet, PatientCreate, patient_login, ambulance_login, PatientViewSet, AmbulancePost, AmbulanceCreate, AmbulanceUpdate, AmbulanceViewSet, TripView

urlpatterns = [
    path(r'hospital/', HospitalViewSet.as_view({'get': 'list'}), name='hospital-all'),
    path(r'patient/', PatientViewSet.as_view({'get': 'list'}), name='patient-all'),
    url(r'ambulance/signup/', AmbulanceCreate.as_view(), name='ambulance-signup'),
    url(r'ambulance/signin/', ambulance_login, name='ambulance-login'),
    path(r'ambulance/', AmbulanceViewSet.as_view({'get': 'list'}), name='ambulance-all'),
    path(r'ambulance/update/', AmbulanceUpdate.as_view(), name='update-location'),
    path(r'ambulance/complete/', AmbulancePost.as_view(), name='complete-trip'),
    path(r'trip/', TripView.as_view(), name='trip-all'),
    url(r'patient/signup/', PatientCreate.as_view(), name='patient-signup'),
    url(r'patient/signin/', patient_login, name='patient-login')
]
