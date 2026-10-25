from flask import Flask, render_template, request, redirect

app = Flask(__name__)
trips = []

@app.route("/")
def home():
    return render_template("index.html", trips=trips)

@app.route("/trips", methods=["POST"])
def add_trip():
    origin = request.form.get("origin")
    destination = request.form.get("destination")
    client = request.form.get("client")
    price = request.form.get("price")
    trips.append({
        "origin": origin, 
        "destination": destination, 
        "client": client, 
        "price": price
    })
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
