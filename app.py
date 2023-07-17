from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create the Flask app
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/eventspin'

# Initialize the SQLAlchemy database
db = SQLAlchemy(app)

# Import your models here
from models import Event, Venue, Organizer, TicketAvailability

# Create the app context and make sure database operations occur within it
with app.app_context():
    # Create all tables
    db.create_all()

@app.route('/')
def hello():
    return 'Hello, World!'

# Add other routes, views, etc. below
# ...

if __name__ == '__main__':
    app.run(port=8000)
