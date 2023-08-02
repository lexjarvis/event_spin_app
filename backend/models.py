# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# def connect_db(app):
#     db.app = app
#     db.init_app(app)

# class EventData(db.Model):
#     __tablename__ = 'event_data'
#     id = db.Column(db.Integer, primary_key=True)
#     event_id = db.Column(db.String(50), unique=True, nullable=False)
#     event_image = db.Column(db.String(200), nullable=True)
#     event_title = db.Column(db.String(200), nullable=False)
#     event_summary = db.Column(db.String(500), nullable=True)
#     event_location = db.Column(db.String(200), nullable=False)
#     event_date = db.Column(db.DateTime, nullable=False)
#     event_start_time = db.Column(db.DateTime, nullable=False)
#     event_end_time = db.Column(db.DateTime, nullable=False)
#     event_cost = db.Column(db.Float, nullable=False)
#     event_age_restriction = db.Column(db.String(50), nullable=True)

#     def __init__(self, event_id, event_image, event_title, event_summary, event_location, event_date,
#                  event_start_time, event_end_time, event_cost, event_age_restriction):
#         self.event_id = event_id
#         self.event_image = event_image
#         self.event_title = event_title
#         self.event_summary = event_summary
#         self.event_location = event_location
#         self.event_date = event_date
#         self.event_start_time = event_start_time
#         self.event_end_time = event_end_time
#         self.event_cost = event_cost
#         self.event_age_restriction = event_age_restriction

# class UserPreferences(db.Model):
#     __tablename__ = 'user_preferences'
#     id = db.Column(db.Integer, primary_key=True)
#     zip_code = db.Column(db.String(10))
#     search_radius = db.Column(db.Integer)
#     event_date = db.Column(db.Date)
#     in_morning = db.Column(db.Boolean, default=False)
#     in_afternoon = db.Column(db.Boolean, default=False)
#     in_evening = db.Column(db.Boolean, default=False)
#     is_free = db.Column(db.Boolean, default=False)
#     is_age_restricted = db.Column(db.Boolean, default=False)

#     def __init__(self, zip_code, search_radius, event_date, in_morning, in_afternoon, in_evening, is_free, is_age_restricted):
#         self.zip_code = zip_code
#         self.search_radius = search_radius
#         self.event_date = event_date
#         self.in_morning = in_morning
#         self.in_afternoon = in_afternoon
#         self.in_evening = in_evening
#         self.is_free = is_free
#         self.is_age_restricted = is_age_restricted


# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()
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

