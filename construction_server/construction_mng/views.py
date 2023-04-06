from django.shortcuts import render
from rest_framework import viewsets, permissions
from construction_mng.models import Worker, Activity, Emergency, Attendance
from construction_mng.serializers import WorkerSerializer, ActivitySerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Create your views here.
class WorkerViewSet(viewsets.ModelViewSet):

    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [permissions.IsAuthenticated]

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]
    


