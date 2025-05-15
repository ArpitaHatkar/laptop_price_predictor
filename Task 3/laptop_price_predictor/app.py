from flask import Flask, render_template, request
from pickle import load

with open("laptop_model.pkl", "rb") as f:
    model = load(f)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    selected = {
        "ram": "",
        "display": "",
        "processor": "",
        "ssd": "",
        "brand": "",
        "gpu": ""
    }
    msg = ""

    if request.method == "POST":
        selected["ram"] = request.form.get("ram")
        selected["display"] = request.form.get("display")
        selected["processor"] = request.form.get("processor")
        selected["ssd"] = request.form.get("ssd")
        selected["brand"] = request.form.get("brand")
        selected["gpu"] = request.form.get("gpu")

        r = int(selected["ram"])
        d = float(selected["display"])
        p = int(selected["processor"])
        s = int(selected["ssd"])
        b = int(selected["brand"])
        g = int(selected["gpu"])

        d1 = [r]
        d2 = [d]
        d3 = [1 if i == p else 0 for i in range(1, 5)]
        d4 = [1 if s == 1 else 0, 1 if s == 2 else 0]
        d5 = [1 if i == b else 0 for i in range(1, 6)]
        d6 = [1 if i == g else 0 for i in range(1, 4)]

        d = [d1 + d2 + d3 + d4 + d5 + d6]
        price = model.predict(d)[0]
        msg = f"Price = ₹ {round(price, 2)}"

    return render_template("home.html", msg=msg, selected=selected)

if __name__ == "__main__":
    app.run(debug=True)
