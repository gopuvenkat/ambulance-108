from django.urls import path
from django.conf.urls import include, url
from .views import HospitalViewSet, PatientCreate, login, PatientViewSet, AmbulanceViewSet

urlpatterns = [
    path(r'api/hospital/', HospitalViewSet.as_view({'get': 'list'}), name='hospital-all'),
    path(r'api/patient/', PatientViewSet.as_view({'get': 'list'}), name='patient-all'),
    path(r'api/ambulance/', AmbulanceViewSet.as_view({'get': 'list'}), name='ambulance-all'),
    url(r'api/signup/', PatientCreate.as_view(), name='patient-signup'),
    url(r'api/signin/', login, name='patient-login')
]
