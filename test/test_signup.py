
import requests
import json
from config import *


def test_signup_empty():
    reqdata = {
        "username": "",
        "password": "",
        "first_name": "",
        "last_name": ""
    }
    resp = requests.post(
        SIGNUP_ENDPOINT, 
        data=json.dumps(reqdata), headers=HEADERS)
    assert resp.status_code == 400

def test_signup_new_user():
    reqdata = {
        "username": USERNAME,
        "password": PASSWORD,
        "first_name": FIRST_NAME,
        "last_name": LAST_NAME
    }
    resp = requests.post(
        SIGNUP_ENDPOINT, 
        data=json.dumps(reqdata), headers=HEADERS)
    resp_data = resp.json()
    print(resp.json())
    error_msg = 'user with this username already exists.'
    if error_msg in resp_data['username']:
        #username already exists
        assert resp.status_code == 400
    else:
        assert resp.status_code == 201
    