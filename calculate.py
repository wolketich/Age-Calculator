import time
from calendar import isleap

def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False