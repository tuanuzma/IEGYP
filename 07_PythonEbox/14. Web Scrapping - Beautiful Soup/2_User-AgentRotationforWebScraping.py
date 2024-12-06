import requests
from itertools import cycle

# List of user-agent strings
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.1.2 Safari/602.3.12'
]

# Create a cyclic iterator for user agents
user_agent_cycle = cycle(user_agents)

# Function to make a request with the next user agent
def make_request(url):
    # Get the next user-agent from the cyclic iterator
    user_agent = next(user_agent_cycle)
    headers = {'User-Agent': user_agent}
    
    # Send a GET request to the URL
    response = requests.get(url, headers=headers)
    
    # If the request is successful, print the user-agent used
    if response.status_code == 200:
        return f'{{\n  "user-agent": "{user_agent}"\n}}'
    else:
        return None

# Input URL from the user
url = input("Enter the URL to scrape: ")

# Make the request and display the scraped data
scraped_data = make_request(url)
if scraped_data:
    print(f"Scraped Data:\n{scraped_data}")
else:
    print("Failed to retrieve data")
