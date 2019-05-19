## Step 2 - MongoDB and Flask Application
# 
# Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

#%%
#Dependencies
import pymongo
from flask import Flask

from scrape_mars import scrape 
#%%
# * Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

app = Flask(__name__)

@app.route("/scrape")
def Scrape():
    print("Server received request for '/scrape' page.\nCalling function scrape() from scrape_mars.py...")
    return dict

if __name__ == "__main__":
    app.run(debug=True)
#%%
# # * Store the return value in Mongo as a Python dictionary.
#%%
# * Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.
@app.route("/")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"
if __name__ == "__main__":
    app.run(debug=True)
#%%
# * Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

#![final_app_part1.png](Images/final_app_part1.png)
#![final_app_part2.png](Images/final_app_part2.png)