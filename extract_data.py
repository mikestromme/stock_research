import requests
from bs4 import BeautifulSoup
import pandas as pd

# List of 10-K filing URLs
filings = [
    "https://www.sec.gov/Archives/edgar/data/320193/000032019323000106/0000320193-23-000106-index.htm",
    # ... other filing URLs ...
]

def extract_financial_statement(filing_url, section_title):
    response = requests.get(filing_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # This is a simplistic example; you'll need more sophisticated logic
    # to accurately find and parse the financial statements
    for section in soup.find_all("section"):
        if section_title in section.text:
            # Extract the data from the section
            # Depending on the format, you might need additional parsing here
            data = section.text
            return data

    return None

# Loop through each filing and extract data
for filing in filings:
    balance_sheet = extract_financial_statement(filing, "Consolidated Balance Sheets")
    income_statement = extract_financial_statement(filing, "Consolidated Statements of Income")
    cash_flow_statement = extract_financial_statement(filing, "Consolidated Statements of Cash Flows")

    # Process and store the extracted data
    # ...

# Example of storing data in a DataFrame (you'll need to adjust this based on your actual data extraction)
df = pd.DataFrame({
    'Filing URL': filings,
    'Balance Sheet': balance_sheet,
    'Income Statement': income_statement,
    'Cash Flow Statement': cash_flow_statement
})

print(df)
