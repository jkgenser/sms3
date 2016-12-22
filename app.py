import os
import datetime
from flask import Flask, request, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from twilio.rest import TwilioRestClient as Client
from twilio import twiml

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import Participant, Survey, Ping

twilio_account_sid = app.config['TWILIO_ACCOUNT_SID']
twilio_auth_token = app.config['TWILIO_AUTH_TOKEN']
twilio_number = app.config['TWILIO_NUMBER']
client = Client(twilio_account_sid, twilio_auth_token)


@app.route('/sms', methods=['GET', 'POST'])
def controller():
    from_number, ans = request.values['From']
    ans = request.values['Body']
    p = db.session.query(Participant).filter(Participant.phone_number == from_number).all()[0]
    s_body = db.session.query(Survey).get(p.survey_id).body
    categories = s_body['question'].keys()

    # Redirect down a level if last answer was a root node name
    if ans.upper() in categories:
        return redirect(url_for('subcategory_controller',
                                body=ans, p_id=p.pid, s_id=p.survey_id))

    # If conversation has not expired
    # TODO: make this based on UTC time
    if session.get('conv_expires') > datetime.datetime.now():
        print 'conversation alive'

        # TODO: make this throw a ValueError if literal provided is not an int
        if type(int(ans)) == int:
            child_options = get_child_options(s_body)

        if ans in child_options:
            print 'one of child options is chosen'

            if session['response_logged'] != 1:
                print 'response not yet logged, now log'

                received_time = datetime.datetime.utcnow() - datetime.timedelta(hours=4)
                ping = Ping(p.id, p.survey_id, received_time, ans)
                db.session.add(ping)
                db.session.commit()

                response = twiml.Response()
                response.message('Thanks! We logged your response.')
                session['response_logged'] = 1
                return str(response)

            if session['response_logged'] == 1:
                print 'response already logged'

                response = twiml.Response()
                response.message('There is no survey open, please wait for next prompt.')
                return str(response)

    # TODO: make this based on UTC time
    if session.get('conv_expires') < datetime.datetime.now():
        response = twiml.Response()
        response.message('There is no survey open, please wait for next prompt.')
        return str(response)


@app.route('/sub_category', methods=['GET', 'POST'])
def subcategory_controller():
    ans = request.args['ans']
    p_id = request.args['p_id']
    s_id = request.args['s_id']
    s_body = db.session.query(Survey).get(s_id).body
    first_options = s_body['question'][ans]['options'].keys()



def get_child_options(s_body):
    child_options = []
    for parent_option in s_body['question'].keys():
        for child_option in s_body['question'][parent_option]['options'].keys():
            child_options.append(child_option)
    return child_options
