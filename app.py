from flask import Flask, render_template
from data_uzivatele import uzivatele
from auth import auth_bp

app = Flask(__name__)

app.register_blueprint(auth_bp)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/admin")
def admin():
    return render_template("admin.html", uzivatele=uzivatele)

if __name__ == "__main__":
    app.run(debug=True)