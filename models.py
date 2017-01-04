from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import JSON


class Participant(db.Model):
    __tablename__ = 'participant'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    survey_id = db.Column(db.Integer, ForeignKey('survey.id'))
    name = db.Column(db.String)
    phone_number = db.Column(db.String)
    role = db.Column(db.String)

    survey = db.relationship('Survey', backref='participants')

    def __init__(self, name, phone_number, role, survey_id):
        self.name = name
        self.phone_number = phone_number
        self.role = role
        self.survey_id = survey_id


class Survey(db.Model):
    __tablename__ = 'survey'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    survey_type = db.Column(db.String)
    body = db.Column(JSON)

    def __init__(self, survey_type, body):
        self.survey_type = survey_type
        self.body = body


class Ping(db.Model):
    __tablename__ = 'ping'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'))
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'))
    sent_time = db.Column(db.DateTime)
    received_time = db.Column(db.DateTime)
    received_num = db.Column(db.String)
    response_value = db.Column(db.String)

    def __init__(self, participant_id, survey_id, received_time=None, response_value=None,
                 sent_time=None):
        self.participant_id = participant_id
        self.survey_id = survey_id
        self.received_time = received_time
        self.response_value = response_value
        self.sent_time = sent_time

    def __repr__(self):
        return 'p :{}, s: {}, t: {}'.format(self.participant_id, self.survey_id, self.sent_time)

