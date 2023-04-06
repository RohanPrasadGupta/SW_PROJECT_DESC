from rest_framework import serializers
from construction_mng.models import Worker, Activity, Emergency, Attendance
import construction_mng.info as info
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    emergency_case = serializers.IntegerField(default=0)

    class Meta:
        model = Activity
        fields = ['worker_id', 'lat', 'lon', 'emergency_case']

    def create(self, validated_data):
        # create a new activity
        worker_id = validated_data['worker_id']
        lat = validated_data['lat']
        lon = validated_data['lon']
        if lat == 0 and lon == 0:
            lat, lon = info.get_lat_lon(worker_id)
        activity = last_activity = info.get_today_last_activity(worker_id)
        is_onsite = info.is_on_site(lat, lon)
        if not last_activity or last_activity.on_site != is_onsite:
            activity = Activity()
            activity.worker_id = worker_id
            activity.lat = lat
            activity.lon = lon
            activity.on_site = is_onsite
            activity.save()
        
        # update lat and lon of worker
        worker = Worker.objects.get(pk = worker_id)
        worker.lat, worker.lon = lat, lon
        worker.save()

        # create or update attendance
        attendance = info.get_today_attendance(worker_id)
        if not attendance:
            # create a new attendance with today date
            attendance = Attendance()
            attendance.worker_id = worker_id
        attendance.save()

        # create the emergency if emergency happens
        self.emergency_case = validated_data["emergency_case"]
        if self.emergency_case != 0:
            emergency = Emergency()
            emergency.worker_id = worker_id
            emergency.lat, emergency.lon = lat, lon
            emergency.case_type = self.emergency_case
            emergency.on_site = is_onsite
            emergency.save()
        return activity
    
class EmergencySerializer(serializers.ModelSerializer):
    worker_id = serializers.PrimaryKeyRelatedField(queryset=Worker.objects.all())
    
    class Meta:
        model = Emergency
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Attendance
        fields = '__all__'
