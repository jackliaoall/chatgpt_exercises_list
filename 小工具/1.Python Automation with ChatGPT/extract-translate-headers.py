.

import requests
from bs4 import BeautifulSoup
import googletrans

# get web page
url = "http://example.com"
response = requests.get(url)

# parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# extract headers
headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

# translate and save
translator = googletrans.Translator()

with open('headers.html', 'w') as f:
    for h in headers:
        translation = translator.translate(h.text, dest="es").text
        f.write(f"<{h.name}>{translation}</{h.name}>\n")