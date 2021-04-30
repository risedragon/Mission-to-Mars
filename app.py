from flask import Flask, render_template, url_for, redirect
#from flask_pymongo import PyMongo
import scraping
import pymongo
from config import mongodb_password

app = Flask(__name__)
# Use flask_pymongo to set up mongo connection
mongo = pymongo.MongoClient(f'mongodb://root:{mongodb_password}@localhost')
db = mongo.mars_app

@app.route("/")
def index():
   mars = db.mars.find_one()
   return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
   mars_data = scraping.scrape_all()
   db.mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

if __name__ == "__main__":
   app.run()