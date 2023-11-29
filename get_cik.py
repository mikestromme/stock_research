import requests

def get_cik_from_ticker(ticker):
    # Endpoint for the SEC's CIK lookup
    url = 'https://www.sec.gov/files/company_tickers.json'

    session = requests.Session()
    response = session.get(url, headers={"User-Agent": "Mozilla/5.0"})
    
    # Check if the request was successful
    if response.status_code == 200:
        # Load the JSON data
        cik_data = response.json()
        
        # Iterate through the data to find the ticker
        for info in cik_data.values():
            if info['ticker'].lower() == ticker.lower():
                return info['cik_str']
    else:
        print('Failed to retrieve data')
        return None


if __name__ == '__main__':
    
    # Example usage
    ticker_symbol = 'AAPL'  # Replace with the ticker symbol you are interested in
    cik_number = get_cik_from_ticker(ticker_symbol)
    print(f"The CIK number for {ticker_symbol} is {cik_number}")


