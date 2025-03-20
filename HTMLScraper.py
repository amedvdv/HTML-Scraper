import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def scrape_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all text and links
        data = []
        for item in soup.find_all(['h1', 'h2', 'h3', 'p', 'a', 'span', 'div']):
            text = item.get_text(strip=True)
            link = item.get('href') if item.name == 'a' else None
            if text:
                data.append({'text': text, 'link': link})

        return data

    except requests.exceptions.RequestException as e:
        return {"error": f"Error fetching the URL: {e}"}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            scraped_data = scrape_website(url)
            if "error" in scraped_data:
                return jsonify(scraped_data)
            
            filename = 'scraped_data.json'
            with open(filename, 'w') as json_file:
                json.dump(scraped_data, json_file, indent=4)
            
            return jsonify(scraped_data)
    
    return '''
    <!doctype html>
    <html>
    <head>
        <title>Web Scraper</title>
    </head>
    <body>
        <h2>Enter a website URL to scrape:</h2>
        <form method="post">
            <input type="text" name="url" placeholder="Enter URL" required>
            <button type="submit">Scrape</button>
        </form>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
