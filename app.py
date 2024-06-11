from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from views import dashboard, country_data

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///covid19.db"
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard_view():
    return dashboard()

@app.route("/country/<string:country_code>")
def country_view(country_code):
    return country_data(country_code)

if __name__ == "__main__":
    app.run(debug=True)
