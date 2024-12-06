from bs4 import BeautifulSoup

# Step 1: Load the HTML file
with open('sample.html', 'r') as html_file:
    content = html_file.read()

# Step 2: Create a BeautifulSoup object and parse the content
soup = BeautifulSoup(content, 'html.parser')

# Step 3: Find all tags with the class "tag"
tags = soup.find_all('a', class_='tag')

# Step 4: Extract and print each tag's text content
for tag in tags:
    print(tag.text)