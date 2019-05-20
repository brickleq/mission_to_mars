## Step 2 - MongoDB and Flask Application

# Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

# * Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

import pandas as pd
import requests
import splinter
import selenium
import time
import platform
from bs4 import BeautifulSoup as bs
from splinter import Browser
from selenium import webdriver

def scrape():
    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)
    soup = bs(response.text,'lxml')
    title = soup.find('div',class_='content_title')
    article_title = title.text
    paragraph = soup.find('div',class_='rollover_description_inner')
    article_paragraph = paragraph.text
    browser = Browser('chrome')
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(5)
    browser.find_by_id('full_image').click()
    time.sleep(5)
    browser.find_link_by_partial_href('spaceimages/details.php?').click()
    time.sleep(5)
    browser.find_link_by_partial_href('hires.jpg').click()
    featured_image_url = browser.url
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    twitter = browser.html
    soup = bs(twitter, 'lxml')
    i = 0
    tweet = soup.find('p', class_='TweetTextSize')
    tweet = tweet.text.split('pic.twitter.com')[0]
    while tweet.startswith('InSight sol 1') == False:
        i+=1; tweet = soup.find('p', class_='TweetTextSize')[i]
    mars_weather = tweet
    url = 'https://space-facts.com/mars/'
    response = requests.get(url)
    soup = bs(response.text,'html.parser')
    html_string = soup.find('table')
    html_table_string = pd.read_html(str(html_string))
    html_table_string = str(html_table_string)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    hemispheres = ['Cerberus Hemisphere','Schiaparelli Hemisphere','Syrtis Major Hemisphere','Valles Marineris Hemisphere']
    hemisphere_images = []
    i = 0
    for hemisphere in hemispheres:
        browser.find_link_by_partial_text(' Hemisphere')[i].click(); time.sleep(2)
        browser.find_link_by_text("Original").click();time.sleep(2)
        url = browser.url
        hemisphere_dict = {'url':url,'title':hemisphere}
        hemisphere_images.append(hemisphere_dict)
        browser.back(); time.sleep(2)
        i+=1
    mars_dict = dict()
    mars_dict = {'NASA Mars News': {'Article Title':article_title,'Article Paragraph':article_paragraph},'JPL Featured Image':featured_image_url,'Mars Weather':mars_weather,'Mars Facts':html_table_string,'Mars Hemispheres':hemisphere_images}
    
    return mars_dict