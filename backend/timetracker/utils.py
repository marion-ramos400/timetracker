
from django.contrib.auth import get_user_model
from datetime import datetime
from isoweek import Week
import pendulum

UserModel = get_user_model()

def retrieve_user(username="", userid=None):
    if userid:
        return UserModel.objects.get(pk=userid)
    return UserModel.objects.filter(username=username).first()


def get_datetime_range(month, week):
    curryear = datetime.now().year
    month_f = str(month).zfill(2)
    pdt = pendulum.parse(f"{curryear}-{month_f}-01T00:00")
    week_of_year = pdt.week_of_year + (int(week) - 1)
    start = Week(curryear, week_of_year).monday()
    start = datetime.combine(start, datetime.min.time()) #convert date to datetime object
    end = Week(curryear, week_of_year).saturday()
    end = datetime.combine(end, datetime.min.time()) #convert date to datetime object
    return start, end
