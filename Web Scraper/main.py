import requests
from bs4 import BeautifulSoup

url = '[URL]'  # replace with the URL you want to analyze

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Check title length
title = soup.find('title').string
title_length = len(title)
print(f'Title: {title}\nLength: {title_length}')

# Check meta description
meta_description_tag = soup.find('meta', attrs={'name': 'description'})
if meta_description_tag:
    meta_description = meta_description_tag.get('content')
    meta_description_length = len(meta_description)
else:
    meta_description = None
    meta_description_length = 0
print(f'Meta description: {meta_description}\nLength: {meta_description_length}')

# Check for h1 tag
h1_tags = soup.find_all('h1')
print(f'Number of H1 tags: {len(h1_tags)}')
for tag in h1_tags:
    print(tag.string)

# Check for broken links
for link in soup.find_all('a', href=True):
    try:
        link_url = link['href']
        # Ignore anchor links and mailto links
        if link_url.startswith('#') or link_url.startswith('mailto:'):
            continue
        # If it's a relative link, add the base URL
        elif link_url.startswith('/'):
            link_url = url + link_url
        # Send a head request (server returns only headers and no document body)
        r = requests.head(link_url)
        # Check if the request was successful
        if r.status_code != 200:
            print(f'Broken link: {link_url} (status code: {r.status_code})')
    except requests.exceptions.RequestException as e:
        print(f'Error checking link: {link_url} (error: {e})')
