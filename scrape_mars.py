from bs4 import BeautifulSoup as BS
import requests as req
import pandas as pd
from splinter import Browser
import time
import pandas as pd

def init_browser():
	return Browser('chrome', headless = False)

def scrape() :
	browser = init_browser()
	mars_data = {}

    url = "https://mars.nasa.gov/news"

    browser.visit(url)

    time.sleep(3)

    soup = BS(browser.html. 'html.parser')

    title = soup.find('div', class_='content_title')

    text = soup.find('div', class_='rollover_descripton_inner')

    newsTitle = title.text
    newsText = text.text

    mars_data['News_Title'] = newsTitle
    mars_data["News_Text"] = newsText

    time.sleep(2)

# Picture

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    url_base = 'https://www.jpl.nasa.gov'
    
    browser.visit(url)

    time.sleep(2)

    soup = BS(browser.html. 'html.parser')

    image = soup.find('article', class_='carousel_item').attrs

    style_prop = str(result['style'])
	trim1 = style_prop.replace("background-image:", "")
	trim2 = trim1.replace(" url('", "")
	JPL_image = trim2.replace("');", "")

    JPL_url = url_base + JPL_image

    mars_data['Featured_Image'] = JPL_url

    time.sleep(2)

# Twitter

    url = 'https://twitter.com/marswxreport?lang=en'

    browser.visit(url)

    time.sleep(3)

    soup = BS(browser.html. 'html.parser')

    weather = soup.find('div', class_="js-tweet-text-container")

    tweet = weather.p.text 

    mars_data['Mars_Weather'] = tweet 

#Facts

    url = 'https://space-facts.com/mars/'

    facts = pd.read_html(url)

    grid = facts[0]
    grid.columns = ["", ""]

    table = grid.to_html(index = False)
    mars_data['Mars_Facts'] = table

    time.sleep(2)

# Hemispehres 

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    url_base = "https://astrogeology.usgs.gov"

    browser.visit(url)

    time.sleep(2)

    soup = BS(browser.html. 'html.parser')

    result = soup.find_all('div', class_="item")

    url_list = []

    for y in result:
        link = y.find('a')['href']
        url_list.append(link)
    

    hemisphere_url_images = []

    for x in url_list:
        url = url_base + x
        
        browser.visit(url)
    
        time.sleep(5)
    
        soup = BS(browser.html, 'html.parser')
    
        result1 = soup.find('img', class_="wide-image")
        image = url_base + result1["src"]
    
        result2 = soup.find('h2', class_='title')
        title = result2.text
        title = title.rsplit(' ', 1)[0]
    
        diction = {"Title": title, "Image URL": image}
        hemisphere_url_images.append(diction)
    
        time.sleep(2)
    
    mars_data['Hemisphere_Images'] = hemisphere_url_images

return mars_data

