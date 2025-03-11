
import requests
from requests.auth import HTTPBasicAuth
import json
from config import *

basic_auth = HTTPBasicAuth(USERNAME, PASSWORD)

def test_get_tasks_ok():
    params = {
        "month": 4,
        "week": 1
    }
    resp = requests.get(
        GETTASKS_ENDPOINT, 
        params=params,
        headers=HEADERS,
        auth=basic_auth)
    print(resp.json())
    assert resp.status_code == 200
