from flask import Flask, jsonify, request, send_from_directory
from models import db, EventData, UserPreferences
from flask_migrate import Migrate
import random
import requests
import os
import certifi
from flask_cors import CORS

from models import db

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://alexajarvis:ppboy@localhost:5432/event_spin_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# Initialize the db object
db.init_app(app)

migrate = Migrate(app, db)

def get_events_from_serpapi(api_key, query):
    # SERP API endpoint to search for events
    serpapi_url = 'https://serpapi.com/search.json'

    # Parameters for the API request
    params = {
        "engine": "google_events",
        "q": query,
        "hl": "en",
        "gl": "us",
        "api_key": api_key
    }

    # Make the API request
    response = requests.get(serpapi_url, params=params, verify=certifi.where())
    data = response.json()

    # Extract events from the response
    events = data['events_results']
    return events

# Serve the React app for all routes
@app.route('/')
def serve_react_app():
    return send_from_directory('../frontend/build', 'index.html')

# API endpoint to handle user spin request
@app.route('/spin', methods=['GET', 'POST'])
def spin_wheel():
    if request.method == 'POST':
        data = request.get_json()

        # Fetch events from the SERP API
        serpapi_api_key = 'a46158d9b188f127a070584d2f0270708896f410452a3f71d1335575422444f6'  
        query = "Events in Tampa"
        events_from_serpapi = get_events_from_serpapi(serpapi_api_key, query)

        if not events_from_serpapi:
            # If no events from SERP API, return an error response
            return jsonify({'message': 'No events found from SERP API.'}), 404

        # Randomly select one event from the fetched events list
        selected_event = random.choice(events_from_serpapi)

        # Return the selected event's data as a response to the frontend
        event_data = {
            'event_title': selected_event['title'],
            # 'event_description': selected_event['description'],
            'event_location': selected_event['address'],
            'event_date': selected_event['date'],
            # 'event_time': selected_event['time'],
            'event_link': selected_event['link'],
            'event_image': selected_event['image']
        }

        return jsonify(event_data)

# Optionally, you can serve the static files directly
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(port=8008, debug=True)

