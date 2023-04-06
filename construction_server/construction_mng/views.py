import construction_mng.info as info
from construction_mng.models import Activity, Attendance, Emergency, Worker
from construction_mng.serializers import MyTokenObtainPairSerializer, ActivitySerializer, WorkerSerializer, EmergencySerializer, AttendanceSerializer
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# called by Angular
class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        workers = self.get_queryset()
        data = info.get_worker_list_response(workers)
        return Response(data)

# called by ESP32
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.AllowAny]

class EmergencyViewSet(viewsets.ModelViewSet):
    queryset = Emergency.objects.all()
    serializer_class = EmergencySerializer
    permission_classes = [permissions.AllowAny]

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['get'])
    def overtime(self, request):
        return Response(info.get_overtime_workers())


    


