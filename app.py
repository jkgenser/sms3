import os
import datetime
from flask import Flask, request, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import Participant, Survey, Ping