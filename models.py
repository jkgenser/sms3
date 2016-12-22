from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import JSON


class Participant(db.Model):
    __tablename__ = 'participant'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    phone_number = db.column(db.String)
    role = db.Column(db.String)
    survey_id = db.column(db.Integer, ForeignKey('survey.id'))

    participants = db.relationship('Participant', backref='survey')
    pings = db.relationship('Ping', backref='survey')


class Survey(db.Model):
    __tablename__ = 'survey'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)


class Ping(db.Model):
    __tablename__ = 'ping'

    id = db.Column(db.Integer, primary_key=True)
    survey_id = db.Column(db.Integer, ForeignKey('survey.id'))
    participant_id = db.Column(db.Integer, ForeignKey('participant.id'))
    sent_time = db.Column(db.DateTime)
    received_time = db.Column(db.DateTime)
    response_value = db.Column(db.String)

