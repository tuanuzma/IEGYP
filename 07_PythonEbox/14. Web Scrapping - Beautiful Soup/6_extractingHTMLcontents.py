import requests
from bs4 import BeautifulSoup

# Function to scrape the content inside the given tag
def scrape_tag_content(url, tag):
    try:
        # Ensure the URL has the correct schema (http or https)
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url

        # Send a GET request to fetch the content of the webpage
        response = requests.get(url, timeout=10)  # Added timeout to prevent long wait times

        # Check if the website was loaded successfully
        if response.status_code == 200:
            # Parse the webpage content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all occurrences of the specified tag
            tags = soup.find_all(tag)

            # Check if the tag is present on the website
            if tags:
                # Loop through all found tags
                for tag_content in tags:
                    # Remove all anchor tags (<a>) from the tag content
                    for a in tag_content.find_all('a'):
                        a.decompose()  # Remove the <a> tag entirely

                    # Print the text inside the tag, after removing unwanted elements
                    print(tag_content.get_text().strip())
            else:
                # Print if no tag is found
                print(f"No {tag} tag is present in website")
        else:
            print("Website not found")
    
    except requests.exceptions.MissingSchema:
        print("Invalid URL. Please provide a valid URL (e.g., starting with http:// or https://).")
    except requests.exceptions.RequestException:
        # Handle the case where the website URL is invalid or inaccessible
        print("Website not found")

# Main function
def main():
    try:
        # Input the website URL
        url = input("Enter website URL:\n").strip()
        if not url:
            print("Website not found")
            return

        # Validate the URL by checking if it can be fetched
        try:
            response = requests.get(url, timeout=5)
            if response.status_code != 200:
                print("Website not found")
                return
        except requests.RequestException:
            print("Website not found")
            return

        # Now that the URL is valid, ask for the tag
        tag = input("Enter tag:\n").strip()
        if not tag:
            print("Website not found")
            return

        # Call the function to scrape the content inside the specified tag
        scrape_tag_content(url, tag)

    except EOFError:
        # Handle EOFError when input is not properly provided
        print("Website not found.")

# Entry point of the program
if __name__ == "__main__":
    main()
