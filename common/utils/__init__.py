import mpu
from dashboard.models import Ambulance, Hospital

def get_distance(pos1, pos2):
    (lat1, long1) = pos1
    (lat2, long2) = pos2
    return mpu.haversine_distance((lat1, long1), (lat2, long2))

def get_nearest_ambulance(pos):
    ambulances = Ambulance.objects.all()
    min_dist = float("inf")
    a = None
    for ambulance in ambulances:
        tmp_pos = (ambulance.latitude, ambulance.longitude)
        dist = get_distance(pos, tmp_pos)
        if(dist < min_dist):
            min_dist = dist
            a = ambulance
    return a

def assign_nearest_ambulance(pos):
    ambulance = get_nearest_ambulance(pos)
    ambulance.status = True
    ambulance.save()
    return ambulance

def get_nearest_hospital(pos):
    hospitals = Hospital.objects.all()
    min_dist = float("inf")
    h = None
    for hospital in hospitals:
        tmp_pos = (hospital.latitude, hospital.longitude)
        dist = get_distance(pos, tmp_pos)
        if(dist < min_dist):
            dist = min_dist
            h = hospital
    return h
