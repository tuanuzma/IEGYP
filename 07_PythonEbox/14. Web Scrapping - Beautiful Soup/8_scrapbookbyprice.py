import requests
from bs4 import BeautifulSoup

# Function to scrape the books based on price range
def scrape_books_by_price(min_price, max_price):
    # URL of the website to scrape
    url = 'http://books.toscrape.com/'
    
    # Send a GET request to fetch the content of the webpage
    response = requests.get(url)
    
    # Parse the webpage content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all the articles with class "product_pod"
    books = soup.find_all('article', class_='product_pod')
    
    # List to store books within the price range
    found_books = []
    
    # Iterate over all the books found
    for book in books:
        # Extract the title of the book
        title = book.h3.a['title']
        
        # Extract the price (inside <p> with class 'price_color')
        price_str = book.find('p', class_='price_color').get_text()
        price = float(price_str.replace('£', ''))  # Convert price to float
        
        # Check if the price is within the provided range
        if min_price <= price <= max_price:
            found_books.append((title, price))
    
    # Return the list of books within the price range
    return found_books

# Main function
def main():
    # Input the minimum and maximum price
    print("Enter the minimum amount")
    min_price = float(input())  # Takes input on the next line
    print("Enter the maximum amount")
    max_price = float(input())  # Takes input on the next line
    
    # Call the function to scrape books within the price range
    books = scrape_books_by_price(min_price, max_price)
    
    # Display the results
    if books:
        print(f"Books between £{min_price:.2f} and £{max_price:.2f}:")
        for idx, (title, price) in enumerate(books):
            if idx != 0:  # For all but the first book, print an extra blank line before the title
                print()
            print(f"Title: {title}")
            print(f"Price: £{price:.2f}")
    else:
        print(f"No books found between £{min_price:.2f} and £{max_price:.2f}.")

# Entry point of the program
if __name__ == "__main__":
    main()