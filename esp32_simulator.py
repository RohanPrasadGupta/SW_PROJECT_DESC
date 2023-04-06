import requests
import random
import time

X0, Y0 = 14.078292, 100.602999
X1, Y1 = 14.080311, 100.604901

auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgwNjg3NjA5LCJpYXQiOjE2ODA2ODczMDksImp0aSI6ImQ3MGY5YWIyNDEyODRlMWZhN2JjMjJlZGY1OGQwYjIwIiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJncm91cDMifQ.2zczDX2A92s0Kq8QiFvU7YRe_89JAZUxYJbuk432pFE"
headers = {'Authorization': 'Bearer ' + auth_token, 'Content-Type': 'application/json'}

w3_lat_walk = 14.078292
w3_lon = 100.6034

w4_lat = 14.0795
w4_lon_walk = 100.602999

w5_lat_walk = 14.078292
w5_lon_walk = 100.602999

while True:
    # W003
    data = {}
    data["worker_id"] = "W003"
    data["lat"] = w3_lat_walk
    data["lon"] = w3_lon
    data["emergency_case"] = 0
    print(data)
    w3_lat_walk += 0.0005
    if w3_lat_walk >= X1 + 0.001:
        w3_lat_walk = 14.078292

    #response = requests.post('http://zunzun.pythonanywhere.com/api/activities/', headers=headers, json=data)
    response = requests.post('http://127.0.0.1:8000/api/activities/', headers=headers, json=data)

    # W004
    data = {}
    data["worker_id"] = "W004"
    data["lat"] = w4_lat
    data["lon"] = w4_lon_walk
    data["emergency_case"] = 0 
    print(data)
    w4_lon_walk += 0.0005
    if w4_lon_walk >= Y1 + 0.001:
        w4_lon_walk = 100.602999

    #response = requests.post('http://zunzun.pythonanywhere.com/api/activities/', headers=headers, json=data)
    response = requests.post('http://127.0.0.1:8000/api/activities/', headers=headers, json=data)

    # W005
    data = {}
    data["worker_id"] = "W005"
    data["lat"] = w5_lat_walk
    data["lon"] = w5_lon_walk
    data["emergency_case"] = 0
    print(data)
    w5_lat_walk += 0.0005
    w5_lon_walk += 0.0005
    if w5_lat_walk >= X1 + 0.001:
        w5_lat_walk = 14.078292

    if w5_lon_walk >= Y1 + 0.001:
        w5_lon_walk = 100.602999

    #response = requests.post('http://zunzun.pythonanywhere.com/api/activities/', headers=headers, json=data)
    response = requests.post('http://127.0.0.1:8000/api/activities/', headers=headers, json=data)

    time.sleep(5)

