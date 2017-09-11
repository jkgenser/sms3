import datetime
import random
from app import db
from models import Ping


def gen_dates(start_date, duration):
    """
    yields a vector of days based on the duration provided, excludes
    weekdays.
    """
    for i in range(duration):
        if i > 0:
            # increment date only after the first iteration
            start_date += datetime.timedelta(1)
        if start_date.weekday() < 5:
            yield start_date


def gen_times(date, frequency):
    """
    yields times between 9 and 5 based on frequency given, completely randomly spaced out
    """
    choices = []
    for i in range(480):
        choices.append(i)

    for i in range(frequency):
        new_time = random.choice(choices)
        ping_time = datetime.datetime(year=date.year, month=date.month, day=date.day, hour=9, minute=0)
        ping_time += datetime.timedelta(minutes=new_time)
        yield ping_time


def build_ping_vector(date, frequency):
    ping_choices = []
    ping_set = []

    for i in range(9):
        ping_time = datetime.datetime(year=date.year, month=date.month, day=date.day, hour=9, minute=15)
        ping_time += datetime.timedelta(hours=i)
        ping_choices.append(ping_time)

    for i in range(frequency):
        new_ping = random.choice(ping_choices)
        ping_set.append(new_ping)

    return ping_set


def gen_times_morning(date, frequency):
    """
    yields times
    """
    for i in range(frequency):
        ping_time = datetime.datetime(year=date.year, month=date.month, day=date.day, hour=9, minute=15)
        yield ping_time


def gen_ping_object(start, duration, frequency, survey_id, participant_id, morning=None):
    """
    Create dictionary to hold pings for a given person
    start: datetime.date(year, month, day)
    frequency: integer, number of pings in a day
    survey_id: id of survey
    participant_id: id of participant to add pings for
    """
    pings = {}
    ping_times = []
    start = start
    for day in gen_dates(start, duration):

        # for time in gen_times(day, frequency):
        #     ping_times.append(time)
        ping_set = build_ping_vector(day, frequency)
        ping_times.extend(ping_set)

    pings['ping_times'] = ping_times
    pings['survey_id'] = survey_id
    pings['participant_id'] = participant_id
    return pings


def ping_loader(ping_obj):
    for ping_time in ping_obj['ping_times']:
        # ping = {}
        # ping['sent_time'] = ping_time
        # ping['survey_id'] = ping_obj['survey_id']
        # ping['participant_id'] = ping_obj['participant_id']
        p = Ping(ping_obj['participant_id'],
                 ping_obj['survey_id'],
                 sent_time=ping_time)

        db.session.add(p)
        db.session.commit()
        print 'ping {} added'.format(p)


def get_child_options(s_body):
    child_options = []
    for parent_option in s_body['question'].keys():
        for child_option in s_body['question'][parent_option]['options'].keys():
            child_options.append(child_option)
    return child_options


def get_parent_options(s):
    parent_options = []
    for parent in s['question'].keys():
        parent_options.append(parent)
    return sorted(parent_options)


def cast_ans(ans):
    try:
        return int(ans)
    except ValueError:
        return ans


def datetime_east():
    return datetime.datetime.utcnow() - datetime.timedelta(hours=4)
