# Import dependencies
import os
from time import sleep

import numpy as np
import pandas as pd

import requests
from bs4 import BeautifulSoup

from splinter import Browser


def init_browser():
    path= os.path.join("..","chromedriver.exe")
    executable_path = {"executable_path": path}
    return Browser("chrome", headless=True)

###
# Scraping Websites for Up-to-Date Data
###

def scrape():

    browser= init_browser()

# NASA Mars News
    news_url= "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

    browser.visit(news_url)
    sleep(2)

    response= browser.html
    soup= BeautifulSoup(response, "html.parser")

    news= soup.find_all("li",class_="slide")

    news_title= news[0].select("div.content_title")[0].text.strip()
    news_teaser= news[0].select("div.article_teaser_body")[0].text.strip()

    print(news_title)
    print(news_teaser)
    
# JPL Mars Space Images - Featured Image
    pic_url= "https://www.jpl.nasa.gov"
    pic_url_query= "/spaceimages/?search=&category=Mars"

    browser.visit(pic_url+pic_url_query)
    browser.click_link_by_partial_text("FULL IMAGE")
    html= browser.html

    soup= BeautifulSoup(html,"html.parser")

    feat_pic= soup.find("article",class_="carousel_item")

    feat_pic_url= feat_pic.a['data-fancybox-href']

    img_src_url= pic_url+feat_pic_url

    print(img_src_url)
    print(type(img_src_url))

# Mars Weather
    tweet_url= "https://twitter.com/marswxreport?lang=en"

    response= requests.get(tweet_url)
    soup= BeautifulSoup(response.text, "html.parser")

    tweet_text= soup.find("p",class_="tweet-text")
    tweet_text_extract= tweet_text.find_all('a')
    for i in tweet_text_extract:
        i.extract()

    tweet_text= tweet_text.text

    print(tweet_text)

# Mars Facts
    facts_url= "https://space-facts.com/mars/"

    fact_table= pd.read_html(facts_url)[0]

    fact_html= fact_table.to_html()

    print("HTML Success")

# Mars Hemispheres
    hemisphere_url= "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    response= requests.get(hemisphere_url)
    soup= BeautifulSoup(response.text, "html.parser")

    thumb_list= [i.text for i in soup.select("h3")]

    url_list= []

    window= 1

    for thumb in thumb_list:
        browser.visit(hemisphere_url)
        browser.find_by_text(thumb).click()
        browser.find_by_text("Sample").click()
        url_list.append(browser.windows[window].url)

        window+= 1
    
    print(url_list[0])

    browser.quit()


    d= {
        "news_title": news_title,
        "news_teaser": news_teaser,
        "img_src_url": img_src_url,
        "tweet_text": tweet_text,
        "fact_html": fact_html,
        "url_list0": url_list[0],
        "url_list1": url_list[1],
        "url_list2": url_list[2],
        "url_list3": url_list[3]
    }

    print("Scrape Complete")
    
    return d