# HTML-Scraper

Code sets up a Flask web application that allows users to enter a URL and scrape its content. Here's a brief breakdown of its functionality:

Web Scraping Function (scrape_website):

Sends an HTTP request to the provided URL.
Extracts text content from <h1>, <h2>, <h3>, <p>, <a>, <span>, and <div> elements.
Captures hyperlinks if found in <a> tags.
Returns the extracted data as a list of dictionaries.
Flask Web Application:

Serves a simple web form where users can input a URL.
When the form is submitted (via POST request), it scrapes the provided URL.
Saves the scraped data into a scraped_data.json file.
Displays the extracted data as a JSON response.
Running the App:

The Flask app runs in debug mode, making it easy to test locally.
