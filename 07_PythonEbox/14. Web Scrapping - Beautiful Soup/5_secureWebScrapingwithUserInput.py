import requests
from bs4 import BeautifulSoup
import re

# Function to fetch and parse the URL
def fetch_and_parse(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers, timeout=10)  # Implementing timeout for security
        response.raise_for_status()  # Check for HTTP request errors
        return BeautifulSoup(response.content, 'html.parser')
    except requests.exceptions.RequestException:
        return None

# Function to extract information from the parsed HTML
def extract_info(soup):
    data = {'links': [], 'emails': []}
    
    # Extracting all links
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('http') or href.startswith('/'):
            data['links'].append(href)
    
    # Extracting all email addresses
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', soup.get_text())
    data['emails'] = emails
    
    return data

# Main function to drive the process
def main():
    url = input("Enter the URL to scrape: ")
    
    soup = fetch_and_parse(url)
    
    if soup is None:
        print("Failed to fetch the page. Check the URL or connection.")
    else:
        extracted_data = extract_info(soup)
        print(f"Extracted data: {extracted_data}")

# Call the main function
if __name__ == "__main__":
    main()
   