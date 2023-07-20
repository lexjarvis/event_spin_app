from flask import Flask, jsonify, request
import requests
import random
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://alexajarvis:ppboy@localhost/eventspin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'connect_args': {'options': '-csearch_path=eventspin_schema'}}
db = SQLAlchemy(app)

# Define the UserSpinParameters model
class UserSpinParameters(db.Model):
    # Fields for zip code, search radius, date, time preference, free/paid, age restriction
    id = db.Column(db.Integer, primary_key=True)
    zip_code = db.Column(db.String(10))
    search_radius = db.Column(db.Integer)
    event_date = db.Column(db.Date)
    time_preference = db.Column(db.String(20))  # morning, afternoon, evening
    free_events_only = db.Column(db.Boolean)
    age_restricted = db.Column(db.Boolean)

# Define a route for the root URL
@app.route('/')
def index():
    return 'Hello, World!'

# API endpoint to handle user spin request
@app.route('/spin', methods=['GET', 'POST'])
def spin_wheel():
    if request.method == 'POST':
        data = request.get_json()

        spin_params = UserSpinParameters(
            zip_code=data['zip_code'],
            search_radius=data['search_radius'],
            event_date=data['event_date'],
            time_preference=data['time_preference'],
            free_events_only=data['free_events_only'],
            age_restricted=data['age_restricted']
        )
        db.session.add(spin_params)
        db.session.commit()

        # Call the Eventbrite API to fetch relevant events
        events = fetch_events_from_eventbrite(data['zip_code'], data['search_radius'], data['event_date'], data['time_preference'], data['free_events_only'], data['age_restricted'])

        # Return the randomly selected event details to the user
        if events:
            # Randomly select an event from 'events' list
            selected_event = random.choice(events)
            # Prepare the response with event details
            response_data = {
                'event_name': selected_event['name'],
                'event_summary': selected_event['summary'],
                'event_image_url': selected_event['image_url'],
                'organizer_name': selected_event['organizer']['name'],
                'event_date': selected_event['date'],
                'start_time': selected_event['start_time'],
                'end_time': selected_event['end_time'],
                'event_location': selected_event['location'],
                'event_price': selected_event['price'],
                'age_restricted': selected_event['age_restricted']
            }
            return jsonify(response_data)
        else:
            return jsonify({'message': 'No events found based on your spin parameters'}), 404
    else:
        return jsonify({'message': 'Please make a POST request to this endpoint'}), 405

# Function to fetch events from Eventbrite API
def fetch_events_from_eventbrite(zip_code, search_radius, event_date, time_preference, free_events_only, age_restricted):    # Implement the logic to call the Eventbrite API and fetch relevant events
    # You can use the 'requests' library to make API requests
    # Process the API response and extract relevant event details
    # Return a list of events that match the user's spin parameters
    # For example:
    url = 'https://www.eventbriteapi.com/v3/events/search/'
    headers = {
        'Authorization': 'Bearer VZT7TAAXKVVYCWKGZCQN'
    }
    params = {
        'location.address': zip_code,
        'location.within': f'{search_radius}mi',
        'start_date.keyword': event_date,
        'time': time_preference,
        'price': 'free' if free_events_only else None,
        'age_restriction': age_restricted
    }

    response = requests.get(url, headers=headers, params=params)
    if response.ok:
        events_data = response.json()['events']
        events = []
        for event_data in events_data:
            # Extract relevant event details and add them to 'events' list
            event = {
                'name': event_data['name']['text'],
                'summary': event_data['summary'],
                'image_url': event_data['logo']['url'] if 'logo' in event_data else None,
                'organizer': {
                    'name': event_data['organizer']['name']
                },
                'date': event_data['start']['local'].split('T')[0],
                'start_time': event_data['start']['local'].split('T')[1],
                'end_time': event_data['end']['local'].split('T')[1],
                'location': event_data['venue']['address']['localized_address_display'],
                'price': event_data['ticket_classes'][0]['cost']['display'],
                'age_restricted': event_data['age_restriction']['age_restriction_label'] if 'age_restriction' in event_data else None
            }
            events.append(event)
        return events
    else:
        return None

# Function to create the tables in the database
def create_tables():
    with app.app_context():  # Use the Flask application context here
        db.create_all()

 # Add the code to grant privileges on the schema here
    with app.app_context():  # Use the Flask application context here
        with db.engine.connect() as con:
            # Replace 'alexajarvis' with your desired database user
            grant_sql = text(
                'GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO alexajarvis;'
            )
            con.execute(grant_sql)

            grant_sequence_sql = text(
                'GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO alexajarvis;'
            )
            con.execute(grant_sequence_sql)

# Run the development server
if __name__ == '__main__':
    # Run the database table creation function before starting the server
    create_tables()
    app.run(port=8008, debug=True)

