# import dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():

    browser = init_browser()

    # Set an empty dictionary to hold final findings
    final_dict = {}
    
    # NASA MARS NEWS
    # Set the featured image url and browser
    news_url = "https://mars.nasa.gov/news/"
    # Visit the URL using splinter 
    browser.visit(news_url)
    # time.sleep(1)
    # Create HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    news_soup = BeautifulSoup(html, 'html.parser')
    # Scrape the URL to find the latest news and get the 'title' and 'paragraph' of the latest news
    article = news_soup.find("div", class_='list_text')
    news_title = article.find("div", class_="content_title").text
    news_p = article.find("div", class_ ="article_teaser_body").text
    

    # JPL Mars Space Images - Featured Image
    # URL for getting the featured image
    featured_img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    # Initiate browser to visit the URL
    browser.visit(featured_img_url)
    # time.sleep(1)
    # Click the 'FULL IMAGE' button on the page
    browser.click_link_by_partial_text("FULL IMAGE")
    # Click the 'more info' button on the page
    browser.click_link_by_partial_text("more info")
    # Created HTML object
    featured_html = browser.html
    # Parse HTML with Beautiful Soup
    featured_img_soup = BeautifulSoup(featured_html, 'html.parser')
    # Scrape the webpage to get the 'Featured Image' source
    figure = featured_img_soup.find("figure", class_ = "lede")
    a_tag = figure.find("a")
    img_tag = figure.find("img")
    img_source = img_tag["src"]
    # Base URL
    base_url = "https://www.jpl.nasa.gov"
    # Get the 'featured image URL' by adding the base_url and the featured_image_url
    featured_image_url = base_url + img_source
 

    #MARS FACTS
    # Mars facts web page URL
    facts_url = "https://space-facts.com/mars/"
    # Read HTML tables from the DataFrame
    tables = pd.read_html(facts_url)
    # Scrape the table containing facts about the planet including Diameter, Mass, etc.
    df = tables[0]
    # Rename the column's header
    df.columns = ["Description", "Mars"]
    # Set the index to the 'Description' column
    mars_df = df.set_index(["Description"])
    # Generate HTML tables from the DataFrame
    mars_facts_html = mars_df.to_html()
    # Strip unwanted '/n' tags to clean up the table
    # mars_facts_html = mars_facts_html.replace('\n', '')


    # MARS HEMISPHERE
    # Set the featured image url and browser
    mars_hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemi_url)
    # time.sleep(1)
    # Created HTML object
    mars_html = browser.html
    # Parse HTML with Beautiful Soup
    mars_hemi_soup = BeautifulSoup(mars_html, 'html.parser')
    # Set an empty list to hold the title and image address of the hemispheres
    hemisphere_image_urls = []
    # Scrape all the "div" with "description" as class. This will give an iterable list
    hemispheres = mars_hemi_soup.find_all("div", class_ = "description")
    # Scrape the web page and get the required data
    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text.strip("Enhanced")
        browser.click_link_by_partial_text(title)
        new_html = browser.html
        new_hemi_soup = BeautifulSoup(new_html, 'html.parser')
        part_url = new_hemi_soup.find("img", class_ = "wide-image")["src"]
        base_url = "https://astrogeology.usgs.gov"
        img_url = base_url + part_url
        hemi_info_dict = {"title" : title,
                     "img_url" : img_url}
        hemisphere_image_urls.append(hemi_info_dict)


    # Update the empty dictionary with the findings
    final_dict["news_title"] = news_title
    final_dict["news_p"] = news_p
    final_dict["featured_image_url"] = featured_image_url
    final_dict["mars_facts"] = mars_facts_html
    final_dict["hemisphere_image_urls"] = hemisphere_image_urls
    
    # Close the browser after scraping
    browser.quit()

    # Return results
    return final_dict
