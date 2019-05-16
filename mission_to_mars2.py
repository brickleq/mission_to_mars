
#%%
# Dependencies
import pandas as pd
import requests
import pymongo
import splinter
import selenium
import time
import platform
from bs4 import BeautifulSoup as bs
from splinter import Browser
from selenium import webdriver

#%%
# Set URL, run requests query, convert response to BeautifulSoup
url = 'https://mars.nasa.gov/news/'
response = requests.get(url)
soup = bs(response.text,'lxml')
print(soup.prettify())

#%%
# Get title and paragraph for first news article 
title = soup.find('div',class_='content_title')
article_title = title.text
paragraph = soup.find('div',class_='rollover_description_inner')
article_paragraph = paragraph.text
print(article_title)
print(article_paragraph)

#%%
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

#%%
### Mars Facts
# Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
url = 'https://space-facts.com/mars/'
response = requests.get(url)
soup = bs(response.text,'html.parser')
print(soup.prettify())
#%%
# Use Pandas to convert the data to a HTML table string.
html_string = soup.find('table')
print(html_string)
html_table_string = pd.read_html(str(html_string))
html_table_string
#%%







'''
### Mars Hemispheres

* Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

* You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.

* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.

* Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```

- - -

## Step 2 - MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

  * Store the return value in Mongo as a Python dictionary.

* Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.

* Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

get_ipython().system('[final_app_part1.png](Images/final_app_part1.png)')
get_ipython().system('[final_app_part2.png](Images/final_app_part2.png)')

- - -

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

#%%
