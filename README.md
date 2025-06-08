# Euterpia Travel Companion

Euterpia is a smart web application that helps users discover exciting places around them — from restaurants and cafes to movie theaters and tourist attractions — using real-time geolocation and the Google Places API. It's designed to be lightweight, fast, and interactive, with a clean UI and mobile responsiveness.

---

## Features

- **Auto Geolocation**: Detects user's current location automatically.
- **Nearby Places Discovery**: Fetches and displays nearby places from multiple categories (restaurants, malls, bars, etc.).
- **Favorites System**: Users can save and toggle favorite places (stored via `localStorage`).
- **Search & Sort**: Filter places by name and sort by rating or name.
- **Live Map Embeds**: Each place includes an interactive map preview.
- **Responsive Design**: Fully mobile-friendly UI with Bootstrap and custom CSS.

---

## Tech Stack

- **Frontend**: HTML5, CSS3, Bootstrap 5, Vanilla JavaScript
- **Backend**: Python 3, Flask
- **APIs**: Google Maps & Google Places API
- **Storage**: LocalStorage for favorites

---

## Demo Preview

> _Coming soon: GIFs or screenshots of app functionality_  
_(You can host the app with Render or Vercel and link it here.)_

---

## 📂 Project Structure

euterpia/
├── app.py # Flask backend
├── static/
│ ├── styles.css # Custom CSS
│ └── euterpia.png # Background image
├── templates/
│ └── index.html # Frontend HTML (rendered by Flask)
└── README.md # You're here!

---

## Setup & Run Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/euterpia-travel-companion.git
   cd euterpia-travel-companion

2. **Install Dependencies**
   ```bash
   pip install flask requests
3. **Set Your API Key**
   ```bash
   python euterpia/app.py
4. **Visit in your browser**
   http://127.0.0.1:5000

Future Improvements
- User accounts and login system

- Reviews & comments integration
- Add direction & route planning
- Upload user-generated photos
- Deploy to mobile via PWA (Progressive Web App)
- Host live with a custom domain


**Author**
Mousse Yeshitila
Bachelor of Science in Information Science
University of Maryland


