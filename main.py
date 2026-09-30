from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/kadromuz")
def kadromuz():
    return render_template("kadro.html")

@app.route("/komiteler")
def komiteler():
    return render_template("komite.html")

@app.route("/socialandmail")
def socialandmail():
    return render_template("socialandmail.html")

@app.route("/misyonumuz")
def misyon():
    return render_template("misyon.html")

@app.route("/vizyonumuz")
def vizyon():
    return render_template("vizyon.html")

@app.route("/basvuru")
def basvuru():
    return render_template("basvuru.html")

if __name__ == "__main__":
    app.run(debug=True)