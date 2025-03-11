
import requests
from requests.auth import HTTPBasicAuth
import json
from config import *

basic_auth = HTTPBasicAuth(USERNAME, PASSWORD)

def test_create_task_ok():
    test_data = {
        "user": USERNAME,
        "start_dt": "2025-04-01T7:30",
        "hours": 3,
        "description": "equipment testing",
        "project": "The Science Project" 
    }
    resp = requests.post(
        CREATE_TASK_ENDPOINT, 
        data=json.dumps(test_data),
        headers=HEADERS,
        auth=basic_auth)
    print(resp.json())
    assert resp.status_code == 201


def test_create_task_invalid_user():
    test_data = {
        "user": "somerandomunknownname",
        "start_dt": "2025-04-01T7:30",
        "hours": 3,
        "description": "equipment cleaning",
        "project": "The Science Project" 
    }
    resp = requests.post(
        CREATE_TASK_ENDPOINT, 
        data=json.dumps(test_data),
        headers=HEADERS,
        auth=basic_auth)
    print(resp.json())
    assert resp.status_code == 404
