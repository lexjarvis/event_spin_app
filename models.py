from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define your models here...


class Event(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.Text)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    venue_id = db.Column(db.String(50), db.ForeignKey('venue.id'))
    organizer_id = db.Column(db.String(50), db.ForeignKey('organizer.id'))
    ticket_availabilities = db.relationship('TicketAvailability', backref='event', lazy=True)

class Venue(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(200))
    address = db.Column(db.String(200))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(100))

class Organizer(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.Text)
    website = db.Column(db.String(200))

class TicketAvailability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.String(50), db.ForeignKey('event.id'))
    ticket_type = db.Column(db.String(100))
    quantity_available = db.Column(db.Integer)
    price = db.Column(db.Float)

# Function to show the tables in the database
def show_tables():
    tables = [Event.__tablename__, Venue.__tablename__, Organizer.__tablename__, TicketAvailability.__tablename__]
    print("Tables in the database:")
    for table in tables:
        print(table)

if __name__ == '__main__':
    # Call the function to show the tables when the script is run directly
    show_tables()
