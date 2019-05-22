# Mars Web Scraping
This respository hosts the work done for the University of Denver Bootcamp which utilizes Python, MongoDB, and HTML to scrape various websites and stitch the retrieved information into a website that displays interesting facts and images from Martian reconnaissance.

## Jupyter Notebook
The initial scraping was conducted using a Jupyter Notebook (site_scraping.ipynb). This allowed me to fix code and test it again in real-time in an easier fashion than using the terminal.

## Python Scripts
The Jupyter code was repurposed in the Python scrape.py file, which is called in the app.py file.

The app.py file largely structures the Flask app to serve the webpage and connects to the Mongo Database. It utilizes an HTML template to insert the information, provided by scrape.py, into the webpage, allowing fresh information upon every press of the "Scrape New Data" button.

## HTML
The webpage is comprised simply of HTML for the moment. In trying to add CSS, I ran headlong further and further into desparation that for the purposes of this assignment I added styles into the HTML directly. Future renditions of this webpage (or others like it) will use CSS.

## Images
The images/ folder hosts the requested screenshots - a top and bottom view of the webpage.