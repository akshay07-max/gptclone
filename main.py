from flask import Flask,render_template, jsonify, request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api", methods = ["GET","POST"])
def qa():
    if request.method == "POST":
        # data = {"result": "I am just a text assistant"} 
        return jsonify(data)
    data = {"result": "I am just a text assistant"} 
    return jsonify(data)



app.run(debug=True)