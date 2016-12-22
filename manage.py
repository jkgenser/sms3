from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
from models import Survey, Participant, Ping

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def add_participant(name=None, phone_number=None, role=None, survey_id=None):
    p = Participant(name, phone_number=phone_number, role=role, survey_id=survey_id)
    db.session.add(p)
    db.session.commit()


@manager.command
def add_survey(survey_type=None, body=None):
    import surveys
    s = Survey(survey_type, surveys.surveys[body])
    db.session.add(s)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
