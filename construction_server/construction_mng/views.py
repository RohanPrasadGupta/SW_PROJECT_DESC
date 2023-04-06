import construction_mng.info as info
from construction_mng.models import Activity, Attendance, Emergency, Worker
from construction_mng.serializers import ActivitySerializer, WorkerSerializer, EmergencySerializer
from rest_framework import permissions, viewsets
from rest_framework.response import Response


# Create your views here.

# called by Angular
class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        workers = self.get_queryset()
        data = info.get_worker_list_response(workers)
        return Response(data)

# called by ESP32
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

class EmergencyViewSet(viewsets.ModelViewSet):
    queryset = Emergency.objects.all()
    serializer_class = EmergencySerializer
    permission_classes = [permissions.IsAuthenticated]


    


