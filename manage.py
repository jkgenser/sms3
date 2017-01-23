from app import app, db
import datetime
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from twilio.rest import TwilioRestClient as Client
from models import Survey, Participant, Ping
from app_utils import datetime_east, get_parent_options


manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

twilio_account_sid = app.config['TWILIO_ACCOUNT_SID']
twilio_auth_token = app.config['TWILIO_AUTH_TOKEN']
twilio_number = app.config['TWILIO_NUMBER']
client = Client(twilio_account_sid, twilio_auth_token)


@manager.command
def add_participant(name=None, phone_number=None, role=None, survey_id=None):
    p = Participant(name, phone_number=phone_number, role=role, survey_id=survey_id)
    db.session.add(p)
    db.session.commit()
    print 'participant added!'


@manager.command
def add_survey(survey_type=None, body=None):
    import surveys
    s = Survey(survey_type, surveys.surveys[body])
    db.session.add(s)
    db.session.commit()
    print 'survey added!'


@manager.command
def add_pings(year, month, day, duration, frequency, s_id, p_id):
    from app_utils import gen_ping_object, ping_loader
    start_date = datetime.datetime(int(year), int(month), int(day))

    ping_obj = gen_ping_object(start_date, int(duration), int(frequency), int(s_id), int(p_id))
    ping_loader(ping_obj)


@manager.command
def retrieve_scheduled_pings():
    from sqlalchemy import and_
    minutes_ago = datetime_east() - datetime.timedelta(minutes=12)

    try:
        all_pings = db.session.query(Ping).filter(and_(Ping.sent_time > minutes_ago,
                                                       Ping.sent_time < datetime_east())).all()
    except:
        return

    for ping in all_pings:
        send_prompt(ping)


def send_prompt(ping):
    to = db.session.query(Participant).get(ping.participant_id).phone_number
    s = db.session.query(Survey).get(ping.survey_id).body

    if s['type'] == 'binary':
        msg = s['sent']['1']
        client.messages.create(to=to, from_ = twilio_number, body=msg)
        return

    parent_options = get_parent_options(s)

    # Build and send the prompt based on survey json structure
    prompt = [s['prompt']]
    for option in parent_options:
        text = s['question'][option]['text']
        stub = ''.join(['(', option, '=', text, ') '])
        prompt.append(stub)

    prompt = ''.join(prompt)

    client.messages.create(
        to=to,
        from_=twilio_number,
        body=prompt)
    return


@manager.command
def add_ping_test(s_id, p_id):
    p = Ping(p_id, s_id, sent_time=datetime_east())
    db.session.add(p)
    db.session.commit()
    print 'ping {} added'.format(p)

if __name__ == '__main__':
    manager.run()
