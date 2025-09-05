from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    texto = ""
    if request.method == "POST":
        texto = request.form.get("texto", "")
    return render_template("index.html", texto=texto)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
