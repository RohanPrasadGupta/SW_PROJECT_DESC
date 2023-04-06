from django.db import models

# Create your models here.
class Worker(models.Model):
    id = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=30)
    device_id = models.CharField(max_length=4)
    phone = models.PositiveIntegerField()
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)

class Activity(models.Model):
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    lat = models.FloatField()
    lon = models.FloatField()
    on_site = models.BooleanField(default=False)

class Emergency(models.Model):
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    lat = models.FloatField()
    lon = models.FloatField()
    on_site = models.BooleanField(default=False)
    case_type = models.SmallIntegerField()
    case_status = models.BooleanField(default=False)
    note = models.CharField(max_length=100, default="")

class Attendance(models.Model):
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    check_in = models.TimeField(auto_now_add=True)
    check_out = models.TimeField(auto_now=True)