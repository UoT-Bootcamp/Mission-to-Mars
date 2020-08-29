# Import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pymongo

# Create an instance of Flask
app = Flask(__name__)

# Use flask_pymongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_facts_app"
mongo = PyMongo(app)


@app.route("/scrape")
def scrape():

    mars_data = mongo.db.mars_data

    # Run the scrape function
    mars_database = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mars_data.update({}, mars_database, upsert=True)

    # Redirect back to home page
    return redirect("/", code = 302)

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_data = mongo.db.mars_data.find_one()

    # Return template and data
    return render_template("index.html", mars_data=mars_data)

if __name__ == "__main__":
    app.run(debug = True)
