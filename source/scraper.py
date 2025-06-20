
import requests
from bs4 import BeautifulSoup

from urllib.parse import urljoin, urlparse

from urllib.parse import urljoin, urlparse

def is_article_link(href, base_url):
    full_url = urljoin(base_url, href) #url join ensures href is treated as browser treats it given you were on the base_url page
    parsed_base = urlparse(base_url)#split url into components
    parsed_link = urlparse(full_url)

    # Check if same domain
    if parsed_link.netloc != parsed_base.netloc:
        return False

    # Skip links that don't go to a different page
    if parsed_link.path == parsed_base.path or parsed_link.path in ["/", ""]: #check if empty path or if the path is the same as the base URL
        return False

    # Skip fragments (anchors like #top)
    if parsed_link.fragment:
        return False
   

    return True


def get_blog_urls(blog_url):
    return False


def scrape_url(url):
    return False
    """
    Scrape the given URL and return the content.
    
    Args:
        url (str): The URL to scrape.
        
    Returns:
        str: The content of the page.
    """
    """'''

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch {url}: {response.status_code}")

    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.get_text()
    """