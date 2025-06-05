from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

fake_weather = [
    "Dust storms everywhere",
    "Blizzards with political debates",
    "Sunny and suspiciously quiet",
    "Thunderstorms louder than revolutions"
]

fake_events = {
    "1920": "The world was adjusting after World War I.",
    "1945": "World War II ended.",
    "1969": "Humans landed on the moon.",
    "1984": "Big Brother was watching you.",
    "2000": "Y2K didn't break the world.",
    "2020": "COVID-19 changed the world.",
    "2024": "AI tools took over productivity!"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/history")
def history_data():
    year = request.args.get("year", "2020")
    weather = random.choice(fake_weather)
    event = fake_events.get(year, f"No major records found in {year}.")
    return jsonify({
        "year": year,
        "weather": f"Weather in {year}: {weather}",
        "event": f"Historical Note: {event}"
    })

if __name__ == "__main__":
    app.run(debug=True)




