from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Google Maps API key
API_KEY = 'AIzaSyDhLJgnVNsblOFh6BinWumITpCvVcDiF1w'  # Replace with your actual API key

# Function to fetch places from Google Maps API
def get_places(location, radius=1000):
    # Base URL for the Places API
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&key={API_KEY}'
    
    # Send a request to Google Maps API
    response = requests.get(url)
    
    # Parse the JSON response
    data = response.json()
    
    # Check if the API call is successful
    if data['status'] == 'OK':
        return data['results']
    else:
        return []

@app.route('/')
def home():
    # Default location (latitude, longitude for College Park, MD as an example)
    location = "38.9866,-76.9378"  # This is a default location; you can modify it to get location from user
    places = get_places(location)  # Fetch places based on location
    return render_template('index.html', places=places)

if __name__ == '__main__':
    app.run(debug=True)

