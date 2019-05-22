import os
from datetime import datetime

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

import scrape


#####
# Initialize Flask app
#####

app= Flask(__name__)


#####
# Initialize MongoDB
#####

mongo = PyMongo(app, uri= "mongodb://localhost:27017/mars_app")


#####
# Set routes
#####

@app.route("/")
def index():
    print("Request made to root")
    mars_info= mongo.db.mars_info.find_one()
    return render_template("index.html", mars_info=mars_info)

@app.route("/scrape")
def activate_scrape():
    print("Request made to scrape")
    mars_info= mongo.db.mars_info
    mars_data= scrape.scrape()
    mars_info.update({}, mars_data, upsert= True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)