
#%%
# Dependencies
import pandas as pd
import requests
import pymongo
import splinter
import selenium
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
#%%
browser.find_by_id('full_image').click()
#%%
url = browser.url
response = requests.get(url)
soup = bs(response.text,'lxml')
print(soup.prettify)
#%%
link
#%%

<a class="fancybox" data-description="This image from NASAs Mars Odyssey shows part of the plains of Noachis Terra southwest of Schiaparelli Crater." data-fancybox-group="images" data-fancybox-href="/spaceimages/images/largesize/PIA23217_hires.jpg" data-link="/spaceimages/details.php?id=PIA23217" data-thumbnail="/spaceimages/images/wallpaper/PIA23217-640x350.jpg" data-title="Noachis Terra - False Color">
									<div class="image_and_description_container">
									  <div class="rollover_description">
									    <h3 class="release_date">May 13, 2019</h3>
										<div class="item_tease_overlay">Noachis Terra - False Color</div>
										<div class="overlay_arrow">
										  <img alt="more arrow" src="/assets/images/overlay-arrow.png">
										</div>
									  </div>
									  <div class="img">
										<img alt="Noachis Terra - False Color" title="Noachis Terra - False Color" class="thumb" src="/spaceimages/images/wallpaper/PIA23217-640x350.jpg">
									  </div>
									  <div class="list_text_content">
									    <div class="article_teaser_body">May 13, 2019</div>
										<div class="content_title">
										  Noachis Terra - False Color
										</div>
										<div class="article_teaser_body">
										  This image from NASAs Mars Odyssey shows part of the plains of Noachis Terra southwest of Schiaparelli Crater.
										</div>
									  </div>
									</div>
								  </a>


# Determine current operating system, set path to Chrome application
current_os = platform.system()
if current_os == 'Linux':
    executable_path = {'executable_path':'usr/bin/google-chrome'}
elif current_os == 'Darwin':
    executable_path = {'executable_path':'/Application/Google\ Chrome.app/Contents/MacOS/Google\ Chrome'} 
elif current_os == 'Windows':
    executable_path = {'executable_path':'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'}
else: 
    raise Exception('Sorry, I don\'t know where to find Chrome...')
    path_to_chrome = input('Please enter the path to Chrome (or ^C to exit): ')
    executable_path = {'executable_path':path_to_chrome}
browser = Browser('chrome', **executable_path)

#%%

#%%
### JPL Mars Space Images - Featured Image

executable_path = {'executable_path':'</path/to/chrome>'}

browser = Browser('chrome', **executable_path)

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

featured_image_url = 
#%%
'''

<article alt="Speedster Star Shocks the Galaxy" class="carousel_item" style="background-image: url('/spaceimages/images/wallpaper/PIA17843-1920x1200.jpg');">
			  <div class="default floating_text_area ms-layer">
				<h2 class="category_title">
				  
				</h2>
				<h2 class="brand_title">
				  FEATURED IMAGE
				</h2>
				<h1 class="media_feature_title">
				  Speedster Star Shocks the Galaxy				</h1>
				<div class="description">
				  
				</div>
				<footer>
				  <a class="button fancybox" data-description="The red arc in this infrared image from NASA's Spitzer Space Telescope is a giant shock wave, created by a speeding star known as Kappa Cassiopeiae." data-fancybox-group="images" data-fancybox-href="/spaceimages/images/mediumsize/PIA17843_ip.jpg" data-link="/spaceimages/details.php?id=PIA17843" data-title="Speedster Star Shocks the Galaxy" id="full_image">
					FULL IMAGE
				  </a>
				</footer>
			  </div>
			  <div class="gradient_container_top"></div>
			  <div class="gradient_container_bottom"></div>
			</article>

### JPL Mars Space Images - Featured Image

* Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

* Make sure to find the image url to the full size `.jpg` image.

* Make sure to save a complete url string for this image.

```python
# Example:
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
```

### Mars Weather

* Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called `mars_weather`.

```python
# Example:
mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'
```
'''
#%%
### Mars Facts

* Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Use Pandas to convert the data to a HTML table string.

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


