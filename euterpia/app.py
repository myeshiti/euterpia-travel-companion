from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Google Maps API key
API_KEY = 'AIzaSyAh8sROh894xBQPCGbQTlHhiHUh4hPpcz8'

def get_places_nearby(lat, lng, radius=2000):
    place_types = [
        "restaurant", "shopping_mall", "amusement_park", "bowling_alley",
        "cafe", "bar", "movie_theater", "night_club", "tourist_attraction",
        "hotels"
    ]
    all_results = []
    for t in place_types:
        token = None
        while True:
            params = {
                "location": f"{lat},{lng}",
                "radius": radius,
                "type": t,
                "key": API_KEY
            }
            if token:
                params["pagetoken"] = token

            resp = requests.get(
                "https://maps.googleapis.com/maps/api/place/nearbysearch/json",
                params=params
            )
            data = resp.json()
            if data.get("status") != "OK":
                break

            all_results.extend(data["results"])
            token = data.get("next_page_token")
            if not token:
                break

    # dedupe by place_id
    unique = {p["place_id"]: p for p in all_results}
    return list(unique.values())

@app.route("/")
def home():
    # just serve the page — we'll load places via JS
    return render_template("index.html")

@app.route("/get_places", methods=["POST"])
def get_places():
    payload = request.get_json()
    lat = payload.get("lat")
    lng = payload.get("lng")
    places = get_places_nearby(lat, lng)
    return jsonify(places=places)

if __name__ == "__main__":
    app.run(debug=True)




