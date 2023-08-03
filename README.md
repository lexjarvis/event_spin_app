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


Database Management
API: https://serpapi.com/google-events-api
	JSON output includes structured data for events results and more.
Types of data that will be used for the app:
The Google Events Results API allows a user to scrape events results from a Google Events page. SerpApi is able to make sense of this information and extract: Thumbnail, Title, Address, Date, Link

Schema
Event Table:
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



Table Relationships

EventData Table:
This table stores information about various events.
It has a primary key "id" that uniquely identifies each event.
The "event_title" column stores the title or name of the event (String, max length 100 characters).
The "event_location" column stores the location of the event (String, max length 100 characters).
The "event_date" column stores the date of the event (String, max length 50 characters).
The "event_link" column stores a URL link related to the event (String, max length 200 characters).
The "event_image" column stores the URL of an image associated with the event (String, max length 200 characters).

UserPreferences Table:
This table stores user preferences or settings related to events.
It has a primary key "id" that uniquely identifies each user preference record.
The "location" column stores the preferred location of the user (String, max length 100 characters).

There is an implicit relationship between these two tables based on the "location" attribute.



Design Brief

Project Scope & Overview
Event Spin is a fun and interactive web application that allows users to discover and explore local events happening in their area. The app aims to provide an engaging user experience by incorporating a spinning wheel game that randomly selects an event for the user to attend. The primary objective of the app is to promote local events, increase user engagement, and encourage participation in community activities.

Target Audience 
The target audience for the Event Spin app includes individuals who enjoy exploring and attending various events in their local area. The app aims to cater to a diverse group of users interested in a wide range of events, such as concerts, festivals, workshops, and community gatherings.

Design Goals 
Modern and Engaging Interface: The app should have a modern and visually appealing interface to attract and engage users. The use of dark and vibrant colors will create a dynamic and immersive user experience.

Professional and Playful Tone: The design should strike a balance between professionalism and playfulness. While the app should be taken seriously as a reliable event discovery platform, it should also evoke a sense of excitement and fun.

Clear Call-to-Action: The spinning wheel and "Spin" button should be prominent and visually compelling to encourage users to engage with the app actively.

Intuitive User Experience: The app should be easy to navigate, and event details should be presented in a clear and concise manner. Users should be able to quickly understand how to use the spinning wheel and view event information.


Brand Identity
The app's brand identity should be vibrant, modern, and approachable. It should reflect a sense of excitement and curiosity, encouraging users to explore the local events with a touch of fun and spontaneity. Colors should be bold and eye-catching with a dark and modern theme.

Visual Design
Homepage: The homepage has a simple, dark background gradient (#1c1c1c to #2d2d2d) along with a clean and intuitive layout. The primary text color is white (#fff) to maintain readability and the components are kept minimal with a text input for users to enter their location and a "Spin" button to initiate the wheel game.

Header: The app's header represents the app’s name with a font size of 100px and “Futura” font style. To stand out against the dark background, the header has a subtle text-shadow and color-changing animation, adding a playful and eye-catching touch. 

Input Fields and Buttons: The input fields and buttons will use the "Futura" font and maintain consistent styling across the app. Input fields will have a dark background (#2d2d2d) with white text (#fff), while buttons will have a background color (#61134c) and change to a darker shade (#290920) on hover.

Spinning Wheel: The spinning wheel will have a dark radial gradient (#61134c to #ba4949) with a subtle box-shadow (0 4px 6px rgba(0, 0, 0, 0.2)). The "Spin" button will also have a radial gradient (#961e76 to #ff6464) with a text-shadow (2px 2px 4px rgba(0, 0, 0, 0.2)) for a 3D effect.

Event Card (Popup): The event popup will appear with a dark background (#333) and white text (#fff) to ensure readability. The popup will have a box-shadow (0 2px 6px rgba(0, 0, 0, 0.5)) for a professional look. The "Learn More" button will have a vibrant background color (#ff6464) and change to a slightly brighter shade (#e62096) on hover.

Event Popup: After the user clicks the “Spin” button, the spinning wheel animation should last for approximately three seconds before settling on a randomly selected event. Upon completion of the spin, a sleek event popup should appear with the event details, including the event title, date, time, location, and an image. Users have the option to access the event's website for more information or close out of the popup to respin for a new event. 


User Flow and Interaction:
Ensure that the user flow is straightforward and intuitive. Users should easily understand the purpose of the app, how to input their location, and initiate the spinning wheel game. The spinning animation should be smooth and visually captivating, enticing users to interact with the app repeatedly.


Conclusion:
The Event Spin app's design will captivate users with its modern and playful interface while offering a clean and intuitive experience. The spinning wheel and event popup will be the central elements that provide an interactive way for users to discover and explore events in their preferred location. With its visually appealing design and user-friendly features, the Event Spin app will attract a wide audience of event enthusiasts.



