# event_spin_app
 
# https://serpapi.com/google-events-api

# Project Brief
Event Spin is a simple web application designed to help users explore and choose activities in their local area using a roulette-like spinning wheel. By integrating the Google Events API, EventSpin generates a curated selection of local events in an interactive format, making it easy for users to find fun things to do near them. For my Capstone, I will be developing the frontend and backend of the Event Spin app using ReactJS and Python. 

The goal of this project is to create a creative app concept that could be applied to various other ideas like selecting a restaurant or movie. The people that would be using this app range anywhere from tourists looking for things to do in a new city to busy professionals with limited time for event research and planning. 

Local event data will come from the Google Events API, with the app requesting to retrieve event information based on the user’s locations. This API provides a comprehensive database of events which will enable the app to provide a wide selection of local activities for the user to choose from. 


#Database Schema
EventData Table:
 Table Name: event_data
 Columns:
   id: Integer (Primary Key)
   event_title: String(100) (Not nullable)
   event_location: String(100) (Not nullable)
   event_date: String(50) (Not nullable)
   event_link: String(200) (Not nullable)
   event_image: String(200) (Not nullable)

UserPreferences Table:
 Table Name: user_preferences
 Columns:
   id: Integer (Primary Key)
   location: String(100) (Not nullable)
