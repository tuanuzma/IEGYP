from bs4 import BeautifulSoup

# Sample HTML content (template code, replace with actual content if necessary)
html_content = """
<!DOCTYPE html>
<html>
<head>
<title>Example Domain</title>
</head>
<body>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <a href="https://www.iana.org/domains/example">More information...</a>
</body>
</html>
"""

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all anchor tags and extract the links
for link in soup.find_all('a'):
    print(link.get('href'))