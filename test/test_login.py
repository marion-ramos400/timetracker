
import requests
from requests.auth import HTTPBasicAuth
import json
from config import *


def test_login():
    basic_auth = HTTPBasicAuth(USERNAME, PASSWORD)
    resp = requests.post(
        LOGIN_ENDPOINT, 
        headers=HEADERS,
        auth=basic_auth)
    assert resp.status_code == 200


    