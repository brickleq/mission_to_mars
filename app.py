## Step 2 - MongoDB and Flask Application
# 
# Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

#%%
#Dependencies
import pymongo
from flask import Flask, render_template

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.MarsDB

# * Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

app = Flask(__name__)

@app.route("/scrape")
def Scrape():
    print("Server received request for '/scrape' page.")
    from scrape_mars import scrape 
    mars_dict = scrape()

    db.mission_to_mars.insert_one(mars_dict) # * Store the return value in Mongo as a Python dictionary.
    return "Scraper data stored in MongoDB as a Python dictionary."

# * Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.
@app.route("/")
def home():
    print("Server received request for '/' page...")
    mars_data = db.mission_to_mars.find_one()
    return render_template('index.html', news_title=mars_data['NASA Mars News']['Article Title'],news_paragraph=mars_data['NASA Mars News']['Article Paragraph'],featured_image=mars_data['JPL Featured Image'],mars_weather=mars_data['Mars Weather'],mars_facts=mars_data['Mars Facts'],hemisphere1_title=mars_data['Mars Hemispheres'][0]['title'],hemisphere1_url=mars_data['Mars Hemispheres'][0]['url'],hemisphere2_title=mars_data['Mars Hemispheres'][1]['title'],hemisphere2_url=mars_data['Mars Hemispheres'][1]['url'],hemisphere3_title=mars_data['Mars Hemispheres'][2]['title'],hemisphere3_url=mars_data['Mars Hemispheres'][2]['url'],hemisphere4_title=mars_data['Mars Hemispheres'][3]['title'],hemisphere4_url=mars_data['Mars Hemispheres'][3]['url'])

if __name__ == "__main__":
    app.run(debug=True)