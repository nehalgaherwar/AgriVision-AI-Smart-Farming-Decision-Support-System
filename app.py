from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample Crop Data
crop_data = {
    "Loamy": ["Wheat", "Rice", "Maize"],
    "Sandy": ["Groundnut", "Watermelon", "Millet"],
    "Clay": ["Paddy", "Broccoli", "Cabbage"]
}

pest_data = {
    "Wheat": "Aphids - Use Neem Oil Spray",
    "Rice": "Stem Borer - Use Pheromone Traps",
    "Maize": "Armyworm - Use Organic Pesticide",
    "Groundnut": "Leaf Miner - Neem Extract",
    "Watermelon": "Fruit Fly - Sticky Traps",
    "Millet": "Shoot Fly - Proper Drainage",
    "Paddy": "Brown Planthopper - Light Trap",
    "Broccoli": "Cabbage Worm - Hand Removal",
    "Cabbage": "Diamondback Moth - Organic Spray"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    soil = request.json["soil"]
    crops = crop_data.get(soil, [])
    return jsonify({"crops": crops})

@app.route("/pest", methods=["POST"])
def pest():
    crop = request.json["crop"]
    info = pest_data.get(crop, "No Data Available")
    return jsonify({"pest": info})

@app.route("/profit", methods=["POST"])
def profit():
    area = float(request.json["area"])
    price = float(request.json["price"])
    yield_amt = float(request.json["yield"])

    revenue = area * yield_amt * price
    cost = revenue * 0.4
    profit = revenue - cost

    return jsonify({
        "revenue": revenue,
        "cost": cost,
        "profit": profit
    })

if __name__ == "__main__":
    app.run(debug=True)
