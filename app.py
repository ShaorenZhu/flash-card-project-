from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/product", methods = ["GET","POST"])
def product():
    if request.method == "POST":
        answer = request.form["ans"]
    return render_template("product.html", question = "Test Question")

@app.route("/contribute")
def contribute():
    return render_template("contribute.html")

if __name__ == "__main__":
    app.run(debug=True)
