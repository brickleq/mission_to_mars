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
    #mars_dict = {'NASA Mars News': {'Article Title': '\n\nWhy This Martian Full Moon Looks Like Candy\n\n', 'Article Paragraph': "\nFor the first time, NASA's Mars Odyssey orbiter has caught the Martian moon Phobos during a full moon phase. Each color in this new image represents a temperature range detected by Odyssey's infrared camera.\n"}, 'JPL Featured Image': 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16029_hires.jpg', 'Mars Weather': 'InSight sol 169 (2019-05-18) low -100.6ºC (-149.1ºF) high -17.6ºC (0.4ºF)\nwinds from the S at 4.6 m/s (10.2 mph) gusting to 15.5 m/s (34.7 mph)\npressure at 7.50 hPa', 'Mars Facts': '[                      0                              1\n0  Equatorial Diameter:                       6,792 km\n1       Polar Diameter:                       6,752 km\n2                 Mass:  6.42 x 10^23 kg (10.7% Earth)\n3                Moons:            2 (Phobos & Deimos)\n4       Orbit Distance:       227,943,824 km (1.52 AU)\n5         Orbit Period:           687 days (1.9 years)\n6  Surface Temperature:                  -153 to 20 °C\n7         First Record:              2nd millennium BC\n8          Recorded By:           Egyptian astronomers]', 'Mars Hemispheres': [{'url': 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced', 'title': 'Cerberus Hemisphere'}, {'url': 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced', 'title': 'Schiaparelli Hemisphere'}, {'url': 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced', 'title': 'Syrtis Major Hemisphere'}, {'url': 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced', 'title': 'Valles Marineris Hemisphere'}]}


    db.mission_to_mars.insert_one(mars_dict) # * Store the return value in Mongo as a Python dictionary.
    return "Scraper data stored in MongoDB as a Python dictionary."

# * Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.
@app.route("/")
def home():
    print("Server received request for '/' page...")
    mars_data = db.mission_to_mars.find_one()
    return render_template('index.html', news_title=mars_data['NASA Mars News']['Article Title'],news_paragraph=mars_data['NASA Mars News']['Article Paragraph'],featured_image=mars_data['JPL Featured Image'],mars_weather=mars_data['Mars Weather'],mars_facts=mars_data['Mars Facts'],hemisphere1_title=mars_data['Mars Hemispheres'][0]['title'],hemisphere1_url=mars_data['Mars Hemispheres'][0]['url'],hemisphere2_title=mars_data['Mars Hemispheres'][0]['title'],hemisphere2_url=mars_data['Mars Hemispheres'][0]['url'],hemisphere3_title=mars_data['Mars Hemispheres'][0]['title'],hemisphere3_url=mars_data['Mars Hemispheres'][0]['url'],hemisphere4_title=mars_data['Mars Hemispheres'][0]['title'],hemisphere4_url=mars_data['Mars Hemispheres'][0]['url'])

if __name__ == "__main__":
    app.run(debug=True)
#%%
# * Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

#![final_app_part1.png](Images/final_app_part1.png)
#![final_app_part2.png](Images/final_app_part2.png)