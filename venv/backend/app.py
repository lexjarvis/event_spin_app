from flask import Flask, jsonify, render_template
from models import db, connect_db, EventData, UserPreferences
from flask_migrate import Migrate
import random
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://alexajarvis:ppboy@localhost:5432/event_spin_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
migrate = Migrate(app, db)

def get_events_from_eventbrite(api_key):
    # Eventbrite API endpoint to search for events
    eventbrite_api_url = 'https://www.eventbriteapi.com/v3/events/search/'

    # Parameters for the API request
    params = {
        'location.address': 'San Francisco',  # Change this to your desired location
        'start_date.range_start': '2023-07-31T00:00:00',  # Change this to your desired start date
        'token': api_key,
    }

    try:
        response = requests.get(eventbrite_api_url, params=params)

        if response.status_code == 200:
            data = response.json()
            events = data.get('events', [])
            return events
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return []

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

# Define a route for the root URL
@app.route('/')
def event_search():
    # Update the query to fetch user preferences
    user_preferences = UserPreferences.query.all()
    return render_template("homepage.html")

# API endpoint to handle user spin request
@app.route('/spin', methods=['GET', 'POST'])
def spin_wheel():
    if request.method == 'POST':
        data = request.get_json()

        # Your existing code for saving user preferences to the database goes here

        # Fetch events from the Eventbrite API
        eventbrite_api_key = 'GHNQS246GPNOSS4WTU'  # Replace this with your actual API key
        events_from_eventbrite = get_events_from_eventbrite(eventbrite_api_key)

        if not events_from_eventbrite:
            # If no events from Eventbrite API, return an error response
            return jsonify({'message': 'No events found from Eventbrite API.'}), 404

        # Combine the events from the database and Eventbrite API
        all_events = EventData.query.all() + events_from_eventbrite

        # Randomly select one event from the combined events list
        selected_event = random.choice(all_events)

        # Return the selected event's data as a response to the frontend
        event_data = {
            'event_id': selected_event['event_id'],
            'event_title': selected_event['event_title'],
            'event_summary': selected_event['event_summary'],
            'event_location': selected_event['event_location'],
            'event_date': selected_event['event_date'],
            'event_start_time': selected_event['event_start_time'],
            'event_end_time': selected_event['event_end_time'],
            'event_cost': selected_event['event_cost'],
            'event_age_restriction': selected_event['event_age_restriction']
        }

        return jsonify(event_data)


@app.route('/events', methods=['GET'])
def get_events():
    events = EventData.query.all()

    event_list = []
    for event in events:
        event_data = {
            'event_id': event.event_id,
            'event_title': event.event_title,
            'event_summary': event.event_summary,
            'event_location': event.event_location,
            'event_date': event.event_date,
            'event_start_time': event.event_start_time,
            'event_end_time': event.event_end_time,
            'event_cost': event.event_cost,
            'event_age_restriction': event.event_age_restriction,
            'zip_code': event.zip_code,
            'in_morning': event.in_morning,
            'in_afternoon': event.in_afternoon,
            'in_evening': event.in_evening,
            'is_free': event.is_free,
            'is_age_restricted': event.is_age_restricted,
        }
        event_list.append(event_data)

    return jsonify(event_list)


if __name__ == '__main__':
    app.run(port=8008, debug=True)
