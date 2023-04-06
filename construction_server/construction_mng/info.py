import datetime
from construction_mng.models import Activity, Attendance, Worker, Emergency

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
    if last_activity:
        lat = last_activity.lat
        lon = last_activity.lon
    else:
        lat, lon = 0, 0
    return lat, lon

def get_attendance(worker_id: str, date):
    try:
        attendance = Attendance.objects.filter(worker_id=worker_id).filter(date = date).last()
        return attendance
    except Attendance.DoesNotExist:
        return None
    
def get_today_attendance(worker_id: str):
    return get_attendance(worker_id, get_today_date())

def get_worker_list_response(workers: list):
    data = []
    for worker in workers:
        worker_response = {}
        attendance = get_today_attendance(worker.id)
        emergency = get_emergency(worker.id)
        last_updated = attendance.check_out if attendance else None
        worker_response['id'] = worker.id
        worker_response['name'] = worker.name
        worker_response['device_id'] = worker.device_id
        worker_response['phone'] = worker.phone
        if emergency:
            worker_response['lat'] = worker.lat
            worker_response['lon'] = worker.lon
            worker_response['emergency'] = emergency.case_type
            worker_response['emergency_id'] = int(Emergency.objects.filter(worker_id = worker.id).last().__str__())
        else:
            worker_response['lat'] = worker.lat if attendance else 0
            worker_response['lon'] = worker.lon if attendance else 0
            worker_response['emergency'] = 0
            
        worker_response['on_site'] = is_on_site(worker.lat, worker.lon)
        worker_response['last_updated'] = last_updated
        
        data.append(worker_response)
    return data

def get_emergency(worker_id: str):
    emergency = Emergency.objects.filter(worker_id = worker_id).filter(case_status = 'False').last()
    return emergency


def get_today_date():
    return datetime.date.today()