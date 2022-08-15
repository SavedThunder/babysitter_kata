import math
from datetime import datetime, timedelta, date
# from time import time

MIDNIGHT = datetime.combine(date.today()+timedelta(days=1), datetime.min.time())
END_BOUND = datetime.combine(date.today()+timedelta(days=1), datetime.strptime('04:00:00', '%H:%M:%S').time())
TODAY = datetime.today()
TOMORROW = datetime.today() + timedelta(days=1)


def calculate_period(time_delta, pay_rate):
    if time_delta != 0:
        return math.floor(time_delta) * pay_rate

    return time_delta

def format_times(time: str):
    '''
    Format times as they come in from the react app
    :param time: the time str
    '''
    if time == None:
        return None

    time = datetime.strptime(time, '%H:%M')
    if time.time() >= MIDNIGHT.time() and time.time() <= END_BOUND.time():
        time = datetime.combine(date.today()+timedelta(days=1), time.time())
    else:
        time = datetime.combine(date.today(), time.time())

    return time

def calculate_nightly_charge(start_time, 
                             end_time, 
                             bed_time=None) -> float:

    '''
    Calculate the nightly charge from the times works
    :param start_time: the timestamp the sitter started ($12/hr)
    :param end_time: the timestamp the sitter left ($8/hr)
    :param bed_time: the timestamp for bedtime ($16/hr)
    '''
    # each 'leg' of the night
    nightly_legs = {}

    # can be used to return information to user that they were not paid for hours outside of 5 - 4
    early_flag = False
    late_flage = False

    # If they started before 5 -> they only get paid for working from 5 ->
    if start_time.time() < datetime.strptime('17:00:00', '%H:%M:%S').time():
        start_time = start_time.replace(hour=17, minute=0, second=0)
        early_flag = True

    # if they left late
    print(end_time, datetime.combine(end_time.date()+timedelta(days=1), datetime.strptime('04:00:00', '%H:%M:%S').time()))
    if end_time > datetime.combine(TOMORROW, datetime.strptime('04:00:00', '%H:%M:%S').time()):
        end_time = end_time.replace(hour=4, minute=0, second=0)
        late_flag = True

    print(start_time, bed_time, end_time, MIDNIGHT, END_BOUND)

    # If there was no bedtime or bedtime was between 12 - 4
    if not bed_time or (bed_time >= MIDNIGHT and bed_time <= END_BOUND):
        nightly_legs['first'] = ((MIDNIGHT - start_time).seconds // 3600)
        nightly_legs['second'] = 0
        if end_time >= MIDNIGHT: # last leg only for after midnight
            nightly_legs['last'] = (end_time - MIDNIGHT).seconds // 3600
        else: # no work after midnight
            nightly_legs['last'] = 0
    else: # there is a bedtime
        nightly_legs['first'] = (bed_time - start_time).seconds // 3600
        nightly_legs['second'] = (MIDNIGHT - bed_time).seconds // 3600
        if end_time >= MIDNIGHT: # last leg only for after midnight
            nightly_legs['last'] = (end_time - MIDNIGHT).seconds // 3600
        else: # no work after midnight
            nightly_legs['last'] = 0

    # start and end before midnight w/ no bedtime
    if not bed_time and end_time < MIDNIGHT:
        nightly_legs['first'] = (end_time - start_time).seconds // 3600

    print(nightly_legs)
    return calculate_period(nightly_legs['first'], 12) + \
           calculate_period(nightly_legs['second'], 8) + \
           calculate_period(nightly_legs['last'], 16)