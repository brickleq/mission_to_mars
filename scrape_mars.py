'''
Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

  * Store the return value in Mongo as a Python dictionary.

* Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.

* Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

get_ipython().system('[final_app_part1.png](Images/final_app_part1.png)')
get_ipython().system('[final_app_part2.png](Images/final_app_part2.png)')
'''

### Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

#%%
# Dependencies
import pandas as pd
import pymongo
import requests
import splinter
import selenium
import time
import platform
from bs4 import BeautifulSoup as bs
from flask import Flask
from selenium import webdriver
from splinter import Browser

#%%
# Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

def scrape():

    # Set URL, run requests query, convert response to BeautifulSoup
    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)
    soup = bs(response.text,'lxml')

    # Get title and paragraph for first news article 
    title = soup.find('div',class_='content_title')
    article_title = title.text
    paragraph = soup.find('div',class_='rollover_description_inner')
    article_paragraph = paragraph.text

    # Use Splinter to navigate to JPL Featured Image 
    browser = Browser('chrome')

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(2)
    browser.find_by_id('full_image').click()
    time.sleep(2)
    browser.find_link_by_partial_href('spaceimages/details.php?').click()
    time.sleep(2)
    browser.find_link_by_partial_href('hires.jpg').click()
    featured_image_url = browser.url

    ### Mars Facts
    # Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    url = 'https://space-facts.com/mars/'
    response = requests.get(url)
    soup = bs(response.text,'html.parser')

    # Use Pandas to convert the data to a HTML table string.
    html_string = soup.find('table')
    html_table_string = pd.read_html(str(html_string))

    ### Mars Hemispheres
    # Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    hemispheres = ['Cerberus Hemisphere','Schiaparelli Hemisphere','Syrtis Major Hemisphere','Valles Marineris Hemisphere']
    hemisphere_images = []

    i = 0
    for hemisphere in hemispheres:
        # You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
        browser.find_link_by_partial_text(' Hemisphere')[i].click(); time.sleep(2)
        browser.find_link_by_text("Original").click();time.sleep(2)
        # Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
        url = browser.url
        # Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
        hemisphere_dict = {'url':url,'title':hemisphere}
        hemisphere_images.append(hemisphere_dict)
        browser.back()
        time.sleep(2)
        i+=1

    return hemisphere_images
hemisphere_images = scrape()
print(hemisphere_images)

#%%
#* Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

app = Flask(__name__)

@app.route("/scrape")
def run_scraper():
    print("Server received request for '/scrape' page...")
    return "Welcome to my 'Home' page!"


# 4. Define what to do when a user hits the /about route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"


if __name__ == "__main__":
    app.run(debug=True)



'''
## Step 3 - Submission

To submit your work to BootCampSpot, create a new GitHub repository and upload the following:

1. The Jupyter Notebook containing the scraping code used.

2. Screenshots of your final application.

3. Submit the link to your new repository to BootCampSpot.

## Hints

* Use Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.

* Use Pymongo for CRUD applications for your database. For this homework, you can simply overwrite the existing document each time the `/scrape` url is visited and new data is obtained.

* Use Bootstrap to structure your HTML template.

## Copyright

© 2019 Trilogy Education Services. All Rights Reserved.
'''