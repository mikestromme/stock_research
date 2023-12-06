import requests
from bs4 import BeautifulSoup

def fetch_and_parse_ixbrl(url):
    # Fetching the content of the iXBRL file
    session = requests.Session()
    response = session.get(url, headers={"User-Agent": "Mozilla/5.0"})

    # Parsing the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Printing the first few tags to inspect
    print(soup.prettify()[:3000])  # Adjust the slice as needed to inspect the structure

    # Extracting XBRL data
    # This is a basic extraction. You'll need to adapt it based on the specific XBRL tags you're interested in.
    xbrl_tags = soup.find_all('ix:nonnumeric')
    for tag in xbrl_tags:
        print(tag['name'], tag.text.strip())

# URL of the iXBRL file
url = 'https://www.sec.gov/ix?doc=/Archives/edgar/data/320193/000032019323000106/aapl-20230930.htm'

fetch_and_parse_ixbrl(url)
