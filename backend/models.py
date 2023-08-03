from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EventData(db.Model):
    __tablename__ = 'event_data'

    id = db.Column(db.Integer, primary_key=True)
    event_title = db.Column(db.String(100), nullable=False)
    event_location = db.Column(db.String(100), nullable=False)
    event_date = db.Column(db.String(50), nullable=False)
    event_link = db.Column(db.String(200), nullable=False)
    event_image = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Event: {self.event_title}>'

class UserPreferences(db.Model):
    __tablename__ = 'user_preferences'

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<UserPreference: {self.location}>'

