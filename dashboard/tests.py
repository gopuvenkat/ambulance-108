from django.test import TestCase
from .models import Hospital, Patient, Ambulance, Trip
# Create your tests here.


class HospitalTest(TestCase):
    """
    Test module for Hospital model.
    """
    def setUp(self):
        Hospital.objects.create(name='Sparsh', latitude=12.8070107, longitude=77.6935667)

    def test_hospital(self):
        sparsh = Hospital.objects.get(name='Sparsh')
        self.assertEqual(sparsh.__str__(), 'Sparsh, 12.8070107, 77.6935667')


class PatientTest(TestCase):
    """
    Test module for Patient model.
    """
    def setUp(self):
        Patient.objects.create(name='Grover', dob=None, contact_number='8169804798')

    def test_patient(self):
        grover = Patient.objects.get(name='Grover')
        self.assertEqual(grover.__str__(), 'Grover, None, 8169804798')


class AmbulanceTest(TestCase):
    """
    Test module for Ambulance model.
    """
    def setUp(self):
        Ambulance.objects.create(number_plate='KA 01 AA 007', latitude=3, longitude=3, contact_number='9483164470', status=False)

    def test_patient(self):
        ambulance = Ambulance.objects.get(number_plate='KA 01 AA 007')
        self.assertEqual(ambulance.__str__(), 'KA 01 AA 007, 3.0, 3.0, 9483164470, False')


class TripTest(TestCase):
    """
    Test module for Trip model.
    """
    def setUp(self):
        patient = Patient.objects.create(name='Grover', dob=None, contact_number='8169804798')
        ambulance = Ambulance.objects.create(number_plate='KA 01 AA 007', latitude=3, longitude=3, contact_number='9483164470', status=False)
        hospital = Hospital.objects.create(name='Sparsh', latitude=12.8070107, longitude=77.6935667)
        Trip.objects.create(patient_id=patient, ambulance_id=ambulance, start_latitude=3, start_longitude=3, hospital_id=hospital)

    def test_patient(self):
        patient = Patient.objects.get(name='Grover')
        trip = Trip.objects.get(patient_id=patient)
        self.assertEqual(trip.__str__(), 'Grover, None, 8169804798, KA 01 AA 007, 3.0, 3.0, 9483164470, False, 3.0, 3.0, Sparsh, 12.8070107, 77.6935667')
