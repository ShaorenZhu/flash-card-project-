from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/product")
def product():
    if request.method == "POST":
        answer = request.form["ans"]
    else:
        return render_template("product.html", question = "Test Question", methods = ["POST", "GET"])

@app.route("/contribute")
def contribute():
    return render_template("contribute.html")

if __name__ == "__main__":
    app.run(debug=True)
