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
from app_utils import datetime_east, cast_ans, get_child_options

twilio_account_sid = app.config['TWILIO_ACCOUNT_SID']
twilio_auth_token = app.config['TWILIO_AUTH_TOKEN']
twilio_number = app.config['TWILIO_NUMBER']
client = Client(twilio_account_sid, twilio_auth_token)


@app.route('/sms', methods=['GET', 'POST'])
def controller():
    from_num = request.values['From']
    ans = request.values['Body']
    p = db.session.query(Participant).filter(Participant.phone_number == from_num).all()[0]
    s = db.session.query(Survey).get(p.survey_id).body

    # Redirect down a level if answer is a top node name
    if ans.upper() in s['question'].keys():
        return redirect(url_for('subcategory_controller', ans=ans, p_id=p.id, s_id=p.survey_id))

    # If conversation is in lowest level of the tree
    if session.get('last_answer') in s['question'].keys():

        # If not expired, go to sub-child controller
        if session.get('conv_expires') > datetime_east():
            return redirect(url_for('subchild', ans=ans, p_id=p.id, s_id=p.survey_id))

        # If expired, respond that conversation has expired
        if session.get('conv_expires') < datetime_east():
            response = twiml.Response()
            response.message('Conversation has expired, wait until next prompt.')
            return str(response)


@app.route('/sub_category', methods=['GET', 'POST'])
def subcategory_controller():
    ans = request.args['ans']
    p_id = request.args['p_id']
    s_id = request.args['s_id']
    s = db.session.query(Survey).get(s_id)

    if ans.upper() in s.body['question'].keys():
        send = ['More specifically?: ']
        for option in s.body['question'][ans]['options'].keys():
            stub = ''.join([option, ' (', s.body['question'][ans]['options'][option], ') ', ])
            send.append(stub)

        response = twiml.Response()
        response.message(''.join(send))

        session['conv_expires'] = (datetime_east() + datetime.timedelta(minutes=20))
        session['response_logged'] = 0
        session['last_answer'] = ans

        return str(response)


@app.route('/subchild', methods=['GET', 'POST'])
def subchild():
    ans = request.args['ans']
    p_id = request.args['p_id']
    s_id = request.args['s_id']
    s = db.session.query(Survey).get(s_id)

    casted_ans = cast_ans(ans)
    if type(casted_ans) == int:
        child_options = get_child_options(s.body)
    else:
        response = twiml.Response()
        response.message('Please provide an integer')
        return str(response)

    if ans in child_options:
        print 'one of child options is chosen'

        if session['response_logged'] != 1:
            print 'response not yet logged, now log'

            received_time = datetime_east()
            ping = Ping(p_id, s_id, received_time, ans)
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


