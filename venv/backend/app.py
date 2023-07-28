from flask import Flask, jsonify, render_template, request, send_from_directory
from models import db, connect_db, EventData, UserPreferences
from flask_migrate import Migrate
from serpapi import GoogleSearch
import random
import requests

app = Flask(__name__, static_folder='../frontend/build/static', template_folder='../frontend/build')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://alexajarvis:ppboy@localhost:5432/event_spin_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

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

    # try:
    #     # response = requests.get(serpapi_url, params=params)

    #     print(f"SERP API request URL: {response.url}")
    #     print(f"SERP API response status code: {response.status_code}")

    #     if response.status_code == 200:
    #         data = response.json()
    #         events = data.get('events_results', [])
    #         print(f"Number of events fetched from SERP API: {len(events)}")
    #         print(f"Events fetched: {events}")
    #         return events
    #     else:
    #         print(f"Error: {response.status_code} - {response.text}")
    #         return []

    # except requests.exceptions.RequestException as e:
    #     print(f"Error: {e}")
    #     return []

    data =  {
  "search_metadata": {
    "id": "64c154a1f716eebacf31e15a",
    "status": "Success",
    "json_endpoint": "https://serpapi.com/searches/31e3914d946979b3/64c154a1f716eebacf31e15a.json",
    "created_at": "2023-07-26 17:15:13 UTC",
    "processed_at": "2023-07-26 17:15:13 UTC",
    "google_events_url": "https://www.google.com/search?q=Events+in+Austin&ibp=htl;events&hl=en&gl=us",
    "raw_html_file": "https://serpapi.com/searches/31e3914d946979b3/64c154a1f716eebacf31e15a.html",
    "total_time_taken": 1.85
  },
  "search_parameters": {
    "q": "Events in Austin",
    "engine": "google_events",
    "hl": "en",
    "gl": "us"
  },
  "search_information": {
    "events_results_state": "Results for exact spelling"
  },
  "events_results": [
    {
      "title": "Sips & Sounds 2023",
      "date": {
        "start_date": "Jul 29",
        "when": "Sat, Jul 29, 2 PM"
      },
      "address": [
        "Moody Amphitheater, 1401 Trinity St",
        "Austin, TX"
      ],
      "link": "https://www.austintexas.org/event/sips-%26-sounds-summer-festival-by-coke-studio/374308/",
      "event_location_map": {
        "image": "https://www.google.com/maps/vt/data=x5CZK4Uv9IAdNWCEh7873l3w6lUadYSNaS10VqiJXW2ELJmuYG1rACxHACxMK3iQ3Gd3gibhGO4cVkSv8O6f5mgzuhnz3_UZDt5_28_ArGPU6EDg3O4",
        "link": "https://www.google.com/maps/place//data=!4m2!3m1!1s0x8644b538bc720c67:0x582b04b3a6359876?sa=X&ved=2ahUKEwi6uLbt76yAAxUZmWoFHaTGCyoQ9eIBegQIARAA&hl=en&gl=us",
        "serpapi_link": "https://serpapi.com/search.json?data=%214m2%213m1%211s0x8644b538bc720c67%3A0x582b04b3a6359876&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Austin&type=place"
      },
      "description": "Sips & Sounds is a FREE, family-friendly music festival featuring some of today’s hottest artists in addition to plenty of food, drinks, and good times to be had! See artists like The...",
      "ticket_info": [
        {
          "source": "Songkick.com",
          "link": "http://www.songkick.com/festivals/3569756-sips-sounds/id/41227229-sips--sounds-2023?utm_medium=organic&utm_source=microformat",
          "link_type": "tickets"
        },
        {
          "source": "Bandsintown.com",
          "link": "https://www.bandsintown.com/f/124913-sips-and-sounds-summer-festival-2023?came_from=209",
          "link_type": "tickets"
        },
        {
          "source": "Tickettailor.com",
          "link": "https://www.tickettailor.com/events/cocacola/917828?a=215D",
          "link_type": "tickets"
        },
        {
          "source": "Visit Austin",
          "link": "https://www.austintexas.org/event/sips-%26-sounds-summer-festival-by-coke-studio/374308/",
          "link_type": "more info"
        },
        {
          "source": "KXAN",
          "link": "https://www.kxan.com/calendar/?_escaped_fragment_=/show/?start=2022-07-17#!/details/Sips-Sounds-Summer-Festival-Amplified-by-Coke-Studio/12243737/2023-07-29T14",
          "link_type": "more info"
        }
      ],
      "venue": {
        "name": "Moody Amphitheater",
        "reviews": 571,
        "link": "https://www.google.com/search?hl=en&gl=us&q=Moody+Amphitheater&ludocid=6353176868970403958&ibp=gwp%3B0,7"
      },
      "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRa-dyjWYTFh8qAUmAm8ikMAbayRXAmSmZ8u17wrTwf5deCrsyUuqlWq4k&s",
      "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRs5hXoM4Vkabtd2N0w0YWqJRauRX1gzvbvXXPYPqVU0w&s=10"
    },
    {
      "title": "Sad Summer Festival",
      "date": {
        "start_date": "Jul 26",
        "when": "Wed, Jul 26, 2 – 5 PM"
      },
      "address": [
        "Germania Insurance Amphitheater, 9201 Circuit of the Americas Blvd",
        "Austin, TX"
      ],
      "link": "https://www.austintexas.org/event/sad-summer-festival/371346/",
      "event_location_map": {
        "image": "https://www.google.com/maps/vt/data=Y5F66ZAnyE7BFvYun4Dp_IuZuC73HB3swB5KykqXPkM7nCcNzS-RewD1q-WNKnsG4zVocXtlAWg7fnf5skx-Jo0hMZvU1DwQpxlzdIVyBcdkyV1Y464",
        "link": "https://www.google.com/maps/place//data=!4m2!3m1!1s0x8644b03c9d42c5a7:0x21814b5914d2754d?sa=X&ved=2ahUKEwi6uLbt76yAAxUZmWoFHaTGCyoQ9eIBegQICRAA&hl=en&gl=us",
        "serpapi_link": "https://serpapi.com/search.json?data=%214m2%213m1%211s0x8644b03c9d42c5a7%3A0x21814b5914d2754d&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Austin&type=place"
      },
      "description": "Sad Summer Festival 2023 will feature Taking Back Sunday, The Maine, Pvris, Hot Mulligan & Mom Jeans.",
      "ticket_info": [
        {
          "source": "Bucketlisters.com",
          "link": "https://bucketlisters.com/experience/sad-summer-fest-2023-at-germania-insurance-amphitheater",
          "link_type": "tickets"
        },
        {
          "source": "Songkick.com",
          "link": "https://www.songkick.com/festivals/3529516-sad-summer-fest-taking-back-sunday-the-maine-andrew-mcmahon-more/id/41143242-sad-summer-fest-taking-back-sunday-the-maine-andrew-mcmahon--more-2023?utm_medium=organic&utm_source=microformat",
          "link_type": "tickets"
        },
        {
          "source": "Bandsintown.com",
          "link": "https://www.bandsintown.com/t/104058503?came_from=209",
          "link_type": "tickets"
        },
        {
          "source": "Visit Austin",
          "link": "https://www.austintexas.org/event/sad-summer-festival/371346/",
          "link_type": "more info"
        },
        {
          "source": "KXAN",
          "link": "https://www.kxan.com/calendar/?_escaped_fragment_=/details/A-MIDSUMMER-NIGHTS-DREAM-FREE-SHAKESPEARE-IN-ZILKER-PARK/10218978/2022-05-29T20#!/details/Sad-Summer-Festival-2023-Presented-by-Journeys-Converse/11486360/2023-07-26T14",
          "link_type": "more info"
        }
      ],
      "venue": {
        "name": "Germania Insurance Amphitheater",
        "reviews": 4080,
        "link": "https://www.google.com/search?hl=en&gl=us&q=Germania+Insurance+Amphitheater&ludocid=2414293721220805965&ibp=gwp%3B0,7"
      },
      "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUxJZ3oBwNMSl9504yFZGqhMw9cFVnJJ1ro0Jv9HrchXpOkl_rRr2ZFrA&s",
      "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTL3l-yNYYE6mPeXK-iZfzZRPqeXjRALGuRLMZVs2LPhg&s=10"
    },
    {
      "title": "Gary Allan",
      "date": {
        "start_date": "Jul 28",
        "when": "Fri, Jul 28, 6 – 11 PM"
      },
      "address": [
        "Round Rock Amp, 3701 N Interstate Hwy 35",
        "Round Rock, TX"
      ],
      "link": "https://www.austinmonthly.com/events/gary-allan-2/",
      "event_location_map": {
        "image": "https://www.google.com/maps/vt/data=xvrOBenH59sHBZPchg36_voulFe3LsqYSSLpWp7iMXnLi2aZCZ-k8-Z1QT7JwCBnJFSUm9A1o4FnzKKriLExlPQwzpRWEwbhRwLEF1oXZ9qkTuqnKh8",
        "link": "https://www.google.com/maps/place//data=!4m2!3m1!1s0x8644d173878290d9:0xc0500d581bc3e52c?sa=X&ved=2ahUKEwi6uLbt76yAAxUZmWoFHaTGCyoQ9eIBegQIERAA&hl=en&gl=us",
        "serpapi_link": "https://serpapi.com/search.json?data=%214m2%213m1%211s0x8644d173878290d9%3A0xc0500d581bc3e52c&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Austin&type=place"
      },
      "description": "KASE101 & 98.1 KVET Present Country Music Live at Round Rock Amp featuring Gary Allan on Friday, July 28th.",
      "ticket_info": [
        {
          "source": "Bandsintown.com",
          "link": "https://www.bandsintown.com/t/1027516811?came_from=209",
          "link_type": "tickets"
        },
        {
          "source": "Ticketmaster.ca",
          "link": "https://www1.ticketmaster.ca/gary-allan-round-rock-07-28-2023/event/Z7r9jZ1AdrF49",
          "link_type": "tickets"
        },
        {
          "source": "Ticketsmarter.com",
          "link": "https://www.ticketsmarter.com/e/gary-allan-tickets-round-rock-7-28-2023-round-rock-amphitheater/5573162",
          "link_type": "tickets"
        },
        {
          "source": "Eventticketscenter.com",
          "link": "https://www.eventticketscenter.com/gary-allan-round-rock-07-28-2023/5573162/t",
          "link_type": "tickets"
        },
        {
          "source": "KXAN",
          "link": "https://www.kxan.com/calendar/?_escaped_fragment_=/show/?start=2020-03-14#!/details/Gary-Allan/11589436/2023-07-28T18",
          "link_type": "more info"
        }
      ],
      "venue": {
        "name": "Round Rock Amp",
        "reviews": 162,
        "link": "https://www.google.com/search?hl=en&gl=us&q=Round+Rock+Amp&ludocid=13857590725493122348&ibp=gwp%3B0,7"
      },
      "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVrX0Y0V1kToB6EdiRhuguidvtbYyo1klgv02m2XR8mYGN__D7oIAtuTU&s",
      "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStCZYLnnDNW8TAASteKJhTI82SuQLdmKZA89bZeXDr_vL2GxPddKLQiznyVg&s=10"
    },
    {
      "title": "Keb Mo",
      "date": {
        "start_date": "Jul 26",
        "when": "Wed, Jul 26, 2 – 11 PM"
      },
      "address": [
        "The Paramount Theatre, 713 Congress Ave.",
        "Austin, TX"
      ],
      "link": "https://www.austin-theater.com/category_dates.php?category=Jazz+Blues&year=2022&month=9&day=26",
      "event_location_map": {
        "image": "https://www.google.com/maps/vt/data=XiRbfNppWPa8kVeVhEtBRP3v0_FSwjmesdPWTkl2P8LKIaHPQu30svoE4VSmMU3JfcB5mon6Him9zE4YMKozeqHHQiHzpo9PpwJkAKOyzFE9zSdP3TQ",
        "link": "https://www.google.com/maps/place//data=!4m2!3m1!1s0x8644b509e4b5c869:0xfca07edeff6106fa?sa=X&ved=2ahUKEwi6uLbt76yAAxUZmWoFHaTGCyoQ9eIBegQIGRAA&hl=en&gl=us",
        "serpapi_link": "https://serpapi.com/search.json?data=%214m2%213m1%211s0x8644b509e4b5c869%3A0xfca07edeff6106fa&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Austin&type=place"
      },
      "description": "A three-time Grammy-winning Delta Blues musician who knows his stuff! Keb Mo, Paramount Theatre, Austin",
      "ticket_info": [
        {
          "source": "Allevents.in",
          "link": "https://allevents.in/austin/keb-mo/230001792783067",
          "link_type": "tickets"
        },
        {
          "source": "Eventticketscenter.com",
          "link": "https://www.eventticketscenter.com/keb-mo-austin-07-26-2023/5704597/t",
          "link_type": "tickets"
        },
        {
          "source": "Austin Theater",
          "link": "https://www.austin-theater.com/theaters/paramount-theatre-texas/keb-mo.php",
          "link_type": "more info"
        },
        {
          "source": "Stereoboard.com",
          "link": "https://www.stereoboard.com/keb-mo-tickets/austin/2023-07-26",
          "link_type": "more info"
        },
        {
          "source": "RateYourSeats.com",
          "link": "https://www.rateyourseats.com/tickets/events/keb-mo-july-26-2023-4411309",
          "link_type": "more info"
        }
      ],
      "venue": {
        "name": "The Paramount Theatre",
        "reviews": 2345,
        "link": "https://www.google.com/search?hl=en&gl=us&q=The+Paramount+Theatre&ludocid=18203689190063933178&ibp=gwp%3B0,7"
      },
      "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGoVRni7NG_8_e3UNkG9Opkup4sy7j-49X3vAD2qaOTCD2J2pMJwLG6co&s",
      "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnjyBv1SaBd6cCyTR1GxW9sAssKVw5klKFVlki_xeqaNjBcdPl5Z3Rx2S-CA&s=10"
    },
    {
      "title": "NXT Great American Bash",
      "date": {
        "start_date": "Jul 30",
        "when": "Sun, Jul 30, 6:30 – 10:30 PM"
      },
      "address": [
        "H-E-B Center at Cedar Park, 2100 Ave of the Stars",
        "Cedar Park, TX"
      ],
      "link": "https://www.austintexas.org/event/wwe%3A-nxt-live-the-great-american-bash/373687/",
      "event_location_map": {
        "image": "https://www.google.com/maps/vt/data=9i3QLfSy1_Gg4xRGyRmpdS9jTN8S-v_ChvrREJACh_6CW-RLDOs7Ym5l0M4acJ2emUxO3zC27S_3r3H9_eqUVANSyVwRpviRu6FQ18wfNDG5JwdT0-4",
        "link": "https://www.google.com/maps/place//data=!4m2!3m1!1s0x865b2cf237fda467:0x15d9f7ecca717524?sa=X&ved=2ahUKEwi6uLbt76yAAxUZmWoFHaTGCyoQ9eIBegQIIRAA&hl=en&gl=us",
        "serpapi_link": "https://serpapi.com/search.json?data=%214m2%213m1%211s0x865b2cf237fda467%3A0x15d9f7ecca717524&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Austin&type=place"
      },
      "description": "WWE bring NXT Great American Bash to Austin, TX on Sunday, July 30th!",
      "ticket_info": [
        {
          "source": "Vividseats.com",
          "link": "https://www.vividseats.com/wwe-nxt-live-tickets-heb-center-at-cedar-park-7-30-2023--sports-wwe/production/4446684?utm_medium=organic&utm_source=google_eventsearch",
          "link_type": "tickets"
        },
        {
          "source": "Koobit.com",
          "link": "https://www.koobit.com/nxt-great-american-bash-cedar-park-e22432/tickets/lower-100-level-79791",
          "link_type": "tickets"
        },
        {
          "source": "Ticketmaster.com",
          "link": "https://ticketmaster.evyy.net/c/253520/271177/4272?u=https%3A%2F%2Fwww.ticketmaster.com%2Fnxt-great-american-bash-cedar-park-texas-07-30-2023%2Fevent%2F3A005EC10E6A7FC5",
          "link_type": "tickets"
        },
        {
          "source": "Visit Austin",
          "link": "https://www.austintexas.org/event/wwe%3A-nxt-live-the-great-american-bash/373687/",
          "link_type": "more info"
        },
        {
          "source": "KXAN",
          "link": "https://www.kxan.com/calendar/?_escaped_fragment_=/show/?start=2020-03-13#!/details/NXT-Great-American-Bash/12097108/2023-07-30T18",
          "link_type": "more info"
        }
      ],
      "venue": {
        "name": "H-E-B Center at Cedar Park",
        "reviews": 4690,
        "link": "https://www.google.com/search?hl=en&gl=us&q=H-E-B+Center+at+Cedar+Park&ludocid=1574562141123474724&ibp=gwp%3B0,7"
      },
      "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdOofB6L4ZIgXrENYPkZ-wxGvJwMBxMeSQNlT5UPgS1VkY070unRn_jHg&s",
      "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTk2e--mW-uq3n6XQySwUA79th7XOklkwLQqePRz0jZMw&s=10"
    },
    {
      "title": "Austin City Limits Music Festival - Weekend One",
      "date": {
        "start_date": "Oct 8",
        "when": "Sun, Oct 8, 12 – 3 PM"
      },
      "address": [
        "Zilker Metropolitan Park",
        "Austin, TX"
      ],
      "link": "https://www.bandsintown.com/e/1028521615-yeah-yeah-yeahs-at-zilker-metropolitan-park",
      "event_location_map": {
        "image": "https://www.google.com/maps/vt/data=9iPGKvsckRjhd9-x5Ic3v29aMmCez_JLSyxn6XUKO-3rliJpOc3bMrxBqMYcXjtfeI6zX_IemIcq39yuUg7s54HralrAO8nwWYpVhXAiYgOeH2qG218",
        "link": "https://www.google.com/maps/place//data=!4m2!3m1!1s0x8644b586e0f968db:0x9b503f3c7a9772ba?sa=X&ved=2ahUKEwi6uLbt76yAAxUZmWoFHaTGCyoQ9eIBegQIKRAA&hl=en&gl=us",
        "serpapi_link": "https://serpapi.com/search.json?data=%214m2%213m1%211s0x8644b586e0f968db%3A0x9b503f3c7a9772ba&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Austin&type=place"
      },
      "description": "Yeah Yeah Yeahs is an alternative rock band formed in New York City in the late summer of 2000. The trio consists of singer/frontwoman Karen O, drummer Brian Chase and guitarist Nick Zinner. Their...",
      "ticket_info": [
        {
          "source": "Aclfestival.com",
          "link": "https://www.aclfestival.com/tickets",
          "link_type": "tickets"
        },
        {
          "source": "Bandsintown.com",
          "link": "https://www.bandsintown.com/t/104414870?came_from=209",
          "link_type": "tickets"
        },
        {
          "source": "Stubhub.ie",
          "link": "https://www.stubhub.ie/austin-city-limits-festival-acl-sunday-pass-tickets-austin-10-8-2023/event/105967024/",
          "link_type": "tickets"
        },
        {
          "source": "Vividseats.com",
          "link": "https://www.vividseats.com/austin-city-limits-festival-tickets-austin-zilker-park-10-8-2023--concerts-music-festivals/production/4158137?utm_medium=organic&utm_source=google_eventsearch",
          "link_type": "tickets"
        },
        {
          "source": "Gametime.co",
          "link": "https://gametime.co/concert/austin-city-limits-festival-sunday-mumford-sons-odesza-hozier-tickets/10-8-2023-austin-tx-zilker-park/events/634ed491f1dd490001892f31?utm_medium=organic&utm_source=microformat",
          "link_type": "tickets"
        }
      ],
      "venue": {
        "name": "Zilker Metropolitan Park",
        "reviews": 3498,
        "link": "https://www.google.com/search?hl=en&gl=us&q=Zilker+Metropolitan+Park&ludocid=11191514603003015866&ibp=gwp%3B0,7"
      },
      "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo6ZRFTerUaMS_bNOvSQJK7wSqLKE6qgLtuh54pWJpPX7AnBtIMcJJzQU&s",
      "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUMr3mzHoRXuKCcYUN-P4f7DjP-KZJoiSB-ci_Ij5NN3Bvd2ZoDuRAlDC6gA&s=10"
    },
    {
      "title": "The Bellamy Brothers",
      "date": {
        "start_date": "Jul 28",
        "when": "Fri, Jul 28, 3 – 6 PM"
      },
      "address": [
        "Buck's Backyard, 1750 Farm to Market 1626",
        "Buda, TX"
      ],
      "link": "https://bucksbackyard.com/event/the-bellamy-brothers/",
      "event_location_map": {
        "image": "https://www.google.com/maps/vt/data=2loLAUXkhisAIWuP9CVQThyxx9BiWR4PfrsX2YxCqfSidA5Z4B9ZMtqQPn94Rx-w4p2NLqLLow6iqAV71jHEplVDqb_NE2QCsT49gYJ43zUTobhYtpI",
        "link": "https://www.google.com/maps/place//data=!4m2!3m1!1s0x865b5187ba3d7beb:0xb47d1dc45903a244?sa=X&ved=2ahUKEwi6uLbt76yAAxUZmWoFHaTGCyoQ9eIBegQIMRAA&hl=en&gl=us",
        "serpapi_link": "https://serpapi.com/search.json?data=%214m2%213m1%211s0x865b5187ba3d7beb%3A0xb47d1dc45903a244&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Austin&type=place"
      },
      "description": "The Bellamy Brothers playing live music at Buck\\'s Backyard in […]\\n",
      "ticket_info": [
        {
          "source": "Eventbrite.com",
          "link": "https://www.eventbrite.com/e/the-bellamy-brothers-tickets-548006731887",
          "link_type": "tickets"
        },
        {
          "source": "Allevents.in",
          "link": "https://allevents.in/buda/the-bellamy-brothers/230003230976970",
          "link_type": "tickets"
        },
        {
          "source": "Buck's Backyard",
          "link": "https://bucksbackyard.com/event/the-bellamy-brothers/",
          "link_type": "more info"
        },
        {
          "source": "Visit Buda",
          "link": "https://www.visitbudatx.com/Calendar.aspx?EID=2014&month=7&year=2023&day=20&calType=0",
          "link_type": "more info"
        },
        {
          "source": "KXAN",
          "link": "https://www.kxan.com/calendar/?_escaped_fragment_=/show/?start=2022-09-28#!/details/LIVE-MUSIC-The-Bellamy-Brothers/12126060/2023-07-28T20",
          "link_type": "more info"
        }
      ],
      "venue": {
        "name": "Buck's Backyard",
        "reviews": 1027,
        "link": "https://www.google.com/search?hl=en&gl=us&q=Buck%27s+Backyard&ludocid=13005584028060066372&ibp=gwp%3B0,7"
      },
      "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5rgA4MawBVsgmukm4ycS9kLFXjVn7FxZ-o4QOjj2sWostIpuq6US643A&s",
      "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRB6rXzl3h6X8Pl7rdgkpj58IbxvdSC-lEpTTRTz1miKA&s=10"
    },
    {
      "title": "2023 H-Town Throwdown",
      "date": {
        "start_date": "Jul 29",
        "when": "Sat, Jul 29, 6 – 11 PM"
      },
      "address": [
        "Round Rock Amp, 3701 N Interstate Hwy 35",
        "Round Rock, TX"
      ],
      "link": "https://www.bandsintown.com/a/12123170-lil-flip",
      "event_location_map": {
        "image": "https://www.google.com/maps/vt/data=xvrOBenH59sHBZPchg36_voulFe3LsqYSSLpWp7iMXnLi2aZCZ-k8-Z1QT7JwCBnJFSUm9A1o4FnzKKriLExlPQwzpRWEwbhRwLEF1oXZ9qkTuqnKh8",
        "link": "https://www.google.com/maps/place//data=!4m2!3m1!1s0x8644d173878290d9:0xc0500d581bc3e52c?sa=X&ved=2ahUKEwi6uLbt76yAAxUZmWoFHaTGCyoQ9eIBegQIORAA&hl=en&gl=us",
        "serpapi_link": "https://serpapi.com/search.json?data=%214m2%213m1%211s0x8644d173878290d9%3A0xc0500d581bc3e52c&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Austin&type=place"
      },
      "description": "Get notified whenever Lil Flip announces a live stream or a concert in your area",
      "ticket_info": [
        {
          "source": "Bandsintown.com",
          "link": "https://www.bandsintown.com/t/1028408993?came_from=209",
          "link_type": "tickets"
        },
        {
          "source": "KXAN",
          "link": "http://kxan.com/calendar/#!/details/2023-H-Town-Throwdown/11633275/2023-07-29T18",
          "link_type": "more info"
        },
        {
          "source": "Eventbrite",
          "link": "https://www.eventbrite.com/e/2023-h-town-throwdown-tickets-550153502937",
          "link_type": "more info"
        },
        {
          "source": "Do512",
          "link": "https://do512.com/events/2023/7/29/h-town-throwdown-2023-tickets",
          "link_type": "more info"
        },
        {
          "source": "SeatGeek",
          "link": "https://seatgeek.com/chamillionaire-tickets",
          "link_type": "more info"
        }
      ],
      "venue": {
        "name": "Round Rock Amp",
        "reviews": 162,
        "link": "https://www.google.com/search?hl=en&gl=us&q=Round+Rock+Amp&ludocid=13857590725493122348&ibp=gwp%3B0,7"
      },
      "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToHE2r1YAhqROyTdvTP62ihksL6VuzcuNyStOpGBG9NEVYQQV-aZanLFM&s",
      "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPC6fDYQtYpYwApMB6gShMum9ClppPAkslghIzCvVbyw&s=10"
    },
    {
      "title": "Austin City Limits Music Festival (October 6-8)",
      "date": {
        "start_date": "Oct 5",
        "when": "Thu, Oct 5 – Sat, Oct 7"
      },
      "address": [
        "Zilker Metropolitan Park",
        "Austin, TX"
      ],
      "link": "https://thebronconation.com/events/austin-city-limits-music-festival-t.18328/",
      "description": "ACL Festival features a diverse lineup of acts every year with 100+ performances. Stop by the Bronco display!",
      "ticket_info": [
        {
          "source": "Livenation.com",
          "link": "https://www.livenation.com/?redirect=false/show/details?id=0&cityname=austin&showdate=2023-10-06&culture=en",
          "link_type": "tickets"
        },
        {
          "source": "KOA",
          "link": "https://koa.com/campgrounds/leander/events/austin-city-limits-music-festival-october-_34a9708c-b3b2-4791-a4ec-acbfca768365/",
          "link_type": "more info"
        },
        {
          "source": "KXAN",
          "link": "https://www.kxan.com/calendar/?_escaped_fragment_=/show/?start=2022-08-20#!/details/Austin-City-Limits-Music-Festival-Weekend-One-/11881298/2023-10-06T11",
          "link_type": "more info"
        },
        {
          "source": "ACL Festival Weekend One - Front Gate Tickets",
          "link": "https://aclfest-weekend1.frontgatetickets.com/event/rzeca9osi34nz9or/passcode/",
          "link_type": "more info"
        },
        {
          "source": "Bandsintown",
          "link": "https://www.bandsintown.com/e/104416191-lil-yachty-at-zilker-metropolitan-park",
          "link_type": "more info"
        }
      ],
      "venue": {
        "name": "Zilker Metropolitan Park",
        "reviews": 3498,
        "link": "https://www.google.com/search?hl=en&gl=us&q=Zilker+Metropolitan+Park&ludocid=11191514603003015866&ibp=gwp%3B0,7"
      },
      "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQLQpyoIxrbuHPdf5Y6mvLJOqoQKYgQjBubokjQbbB75krRSgpC9HS-2CQ&s"
    },
    {
      "title": "DJ Paul, Young Buck",
      "date": {
        "start_date": "Jul 28",
        "when": "Fri, Jul 28, 9:00 AM – 2:59 PM"
      },
      "address": [
        "Antone's Nightclub, 305 E 5th St.",
        "Austin, TX"
      ],
      "link": "https://www.kxan.com/calendar/?_escaped_fragment_=/show/?start=2023-03-30#!/details/Antone-s-Anniversary-DJ-Paul-w-Young-Buck-LATE-SHOW/12034634/2023-07-28T00",
      "event_location_map": {
        "image": "https://www.google.com/maps/vt/data=wJxZY1yzabdXo2CPNtim_lqdX-Q8xzWkyssqUarlKi2mivT3yqEnMarz80fGHQq2XhQc4KEM-SxYOtj6jNPF_O4ck_fUldsOgucvv6BupRjzq5rsWgQ",
        "link": "https://www.google.com/maps/place//data=!4m2!3m1!1s0x8644b5091bd69d65:0x945d683a5e34b71f?sa=X&ved=2ahUKEwi6uLbt76yAAxUZmWoFHaTGCyoQ9eIBegQISRAA&hl=en&gl=us",
        "serpapi_link": "https://serpapi.com/search.json?data=%214m2%213m1%211s0x8644b5091bd69d65%3A0x945d683a5e34b71f&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Austin&type=place"
      },
      "description": "ANTONE'S PRESENTS Antone's 48th Anniversary: DJ Paul w/ Young Buck - LATE SHOW - FRI · JUL 28, 2023 Doors: 10:59 pm / Show: 11:59 pm Tickets: bit.ly/40W5E8S",
      "ticket_info": [
        {
          "source": "Ticketsmarter.com",
          "link": "https://www.ticketsmarter.com/e/dj-paul-tickets-austin-7-28-2023-antones/5771064",
          "link_type": "tickets"
        },
        {
          "source": "Allevents.in",
          "link": "https://allevents.in/austin/eric-gales/230001466008709",
          "link_type": "tickets"
        },
        {
          "source": "KXAN",
          "link": "https://www.kxan.com/calendar/?_escaped_fragment_=/show/?start=2022-09-29#!/details/Antone-s-Anniversary-DJ-Paul-w-Young-Buck-MIDNIGHT-SHOW-/11931350/2023-07-28T09",
          "link_type": "more info"
        }
      ],
      "venue": {
        "name": "Antone's Nightclub",
        "reviews": 1334,
        "link": "https://www.google.com/search?hl=en&gl=us&q=Antone%27s+Nightclub&ludocid=10690815690345330463&ibp=gwp%3B0,7"
      },
      "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRq4sOqGBF3qpYNLJHYVNhEHFuqiE8diCAPsPwPTuQ&s",
      "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQM0-KzLZkjBXjmR3IN_w7z9pNh_rDQd_xtZ5fU_fPF9Q&s=10"
    }
  ]
}
    events = data.get('events_results', [])
    return events


# Define a route for the root URL
@app.route('/')
def event_search():
    query = "Events in Tampa"
    return render_template("homepage.html")

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
            # 'event_location': selected_event['location'],
            'event_date': selected_event['date'],
            # 'event_time': selected_event['time'],
            'event_link': selected_event['link']
        }

        return jsonify(event_data)

@app.route('/')
def serve_react_app():
    return render_template('index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)


if __name__ == '__main__':
    app.run(port=8008, debug=True)