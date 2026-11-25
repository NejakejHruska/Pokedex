from flask import Flask, render_template, session, redirect, url_for, abort
from data_uzivatele import uzivatele
from auth import auth_bp

app = Flask(__name__)

app.register_blueprint(auth_bp)

app.secret_key = 'Pokemon_Tajny_Klic'
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/admin")
def admin():
    if session.get("uzivatel_id") is None:
        return redirect(url_for("auth.login"))

    if session.get("uzivatel_role") != "admin":
        abort(403)

    return render_template("admin.html", uzivatele=uzivatele)

@app.errorhandler(403)
def forbidden(e):
    return render_template("403.html"), 403

if __name__ == "__main__":
    app.run(debug=True)