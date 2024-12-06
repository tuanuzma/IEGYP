from bs4 import BeautifulSoup

# Sample HTML content provided by the template
html_content = """
<html>
  <head>
    <title>Book Store</title>
  </head>
  <body>
    <div class="book-item">
      <h1>A Light in the Attic</h1>
      <a href="catalogue/a-light-in-the-attic_1000/index.html">Book Link</a>
      <p class="price">51.77</p>
    </div>
  </body>
</html>
"""

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Function to extract and print the book name
def find_item_name():
    item_name = soup.find('h1').text
    print(item_name)

# Function to extract and print the book link
def find_item_link():
    item_link = soup.find('a')['href']
    print(item_link)

# Function to extract and print the book price
def find_item_price():
    item_price = soup.find('p', class_='price').text
    print(item_price)

# Call the functions to display item details
find_item_name()
find_item_link()
find_item_price()
