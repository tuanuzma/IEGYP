from bs4 import BeautifulSoup

# Sample HTML input (for illustration purposes)
html_content = '''
<html>
<body>
    <div class="book">
        <h1 class="title">A Light in the Attic</h1>
        <p class="rating">Three</p>
    </div>
</body>
</html>
'''

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Function to find the item name
def find_item_name():
    item_name = soup.find('h1', class_='title').text
    print(item_name)

# Function to find the rating
def rating():
    item_rating = soup.find('p', class_='rating').text
    print(item_rating)

# Call the functions
find_item_name()
rating()
