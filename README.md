# web-scraping-challenge

# *Mission To MARS!!*

In this project, we will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what we need to do.

## Step 1 - Scraping

We will complete our initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

We will create a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all scraping and analysis tasks.

The following outlines what we need to scrape.

### NASA Mars News

* The website we will scrape is - https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest
* We will collect latest News Title and Paragraph Text and will assign these informations to variables 'news_title' and 'news_p' respectively.
* We use Splinter to navigate the website and scrape the required information.

<br/>

![mars](https://github.com/UoT-Bootcamp/web-scraping-challenge/blob/master/Missions_to_Mars/screenshots/latest_mars_news.png)

<br/>

### JPL Mars Space Images - Featured Image

* We will scrape this website for JPL Featured Space Image - https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
* We use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.

<br/>

![mars](https://github.com/UoT-Bootcamp/web-scraping-challenge/blob/master/Missions_to_Mars/screenshots/featured_image.png)

<br/>

### Mars Facts

* We will visit Mars Facts webpage https://space-facts.com/mars/ and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
* We use Pandas to convert the data to a HTML table string.

<br/>

![mars](https://github.com/UoT-Bootcamp/web-scraping-challenge/blob/master/Missions_to_Mars/screenshots/mars_facts.png)

<br/>

### Mars Hemispheres

* We will visit the USGS Astrogeology site https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars to obtain high resolution images for each of Mar's hemispheres.
* We click each of the links to the hemispheres in order to find the image url to the full resolution image and save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. We use a Python dictionary to store the data using the keys img_url and title and then append the dictionary to a list. This list will contain one dictionary for each hemisphere.

<br/>

![mars](https://github.com/UoT-Bootcamp/web-scraping-challenge/blob/master/Missions_to_Mars/screenshots/mars_hemisphere_one.png)

<br/>

![mars](https://github.com/UoT-Bootcamp/web-scraping-challenge/blob/master/Missions_to_Mars/screenshots/mars_hemisphere_two.png)

<br/>

## Step 2 - MongoDb and Flask Application

We use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

The process that involved are:

* Convert the Jupyter notebook into a Python script called scrape_mars.py with a function called 'scrape' that will execute all of the scraping code from above and return one Python dictionary containing all of the scraped data.
* Create a route called '/scrape' that will import the 'scrape_mars.py' script and call the scrape function. Then we store the return value in Mongo as a Python dictionary.
* Create a root route '/' that will query the Mongo database that we created and pass the mars data into an HTML template to display the data.
* Create a template HTML file called 'index.html' that will take the mars data dictionary and display all of the data in the appropriate HTML elements.
