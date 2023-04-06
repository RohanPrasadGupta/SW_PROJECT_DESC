import datetime
from construction_mng.models import Activity, Attendance

X0, Y0 = 1, 1
X1, Y1 = 10, 10

def is_on_site(lat: float, lon: float) -> bool:
    return (X0 <= lat <= X1) and (Y0 <= lon <= Y1)

def get_today_last_activity(worker_id: str):
    today = get_today_date()
    last_activity = Activity.objects.filter(worker_id=worker_id, date = today).last()
    return last_activity


def get_lat_lon(worker_id: str):
    last_activity = Activity.objects.filter(worker_id=worker_id).last()
    lat = last_activity.lat
    lon = last_activity.lon
    return lat, lon

def get_attendance(worker_id: str, date):
    try:
        attendance = Attendance.objects.get(worker_id=worker_id, date=date)
        return attendance
    except Attendance.DoesNotExist:
        return None


def get_today_date():
    return datetime.date.today()