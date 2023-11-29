import requests
from bs4 import BeautifulSoup
from get_cik import get_cik_from_ticker

   
def getFilings(cik):  
    
    # Define the URL for the EDGAR search page
    edgar_search_url = 'https://www.sec.gov/cgi-bin/browse-edgar'


    # Specify the parameters for the search: company name, type of form, etc.
    params = {
        'action': 'getcompany',
        'CIK': cik,  # Replace with actual CIK number of the company
        'type': '10-K',
        'dateb': '',
        'owner': 'exclude',
        'start': '',
        'output': 'atom',
        'count': '10'
    }

    # Send the HTTP request to EDGAR with the specified parameters
    response = requests.get(edgar_search_url, params=params, headers={"User-Agent": "Mozilla/5.0"})

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, features="xml")

        # Find all links to 10-K forms in the feed
        entries = soup.find_all('entry')
        for entry in entries:
            # Extract and print the title and link to the filing
            title = entry.find('title').text
            link = entry.find('link')['href']
            print(f'Title: {title}, Link: {link}')
    else:
        print('Failed to retrieve data')


if __name__ == '__main__':

    getFilings(320193)


