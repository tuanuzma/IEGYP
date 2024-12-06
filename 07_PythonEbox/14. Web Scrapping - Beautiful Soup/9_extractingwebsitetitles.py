import requests
from bs4 import BeautifulSoup

def get_website_info(url):
    try:
        # Send a GET request to the website
        response = requests.get(url)
        
        # Check if the website was found (HTTP status code 200)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract the title of the website
            title = soup.title.string if soup.title else "No title found"
            
            # Check if the website contains an h1 tag
            h1_tag = soup.find('h1')
            if h1_tag:
                print(f"{h1_tag.get_text()}")
            else:
                print("No h1 tag is present in website")
        else:
            print("Website not found")
    except requests.exceptions.RequestException:
        print("Website not found")

# Input: Get the website URL from the user
url = input("Enter website URL:\n")
get_website_info(url)