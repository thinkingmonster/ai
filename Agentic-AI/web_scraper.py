"""Web scraping utility to fetch website contents."""

import requests
from bs4 import BeautifulSoup


def fetch_website_contents(url, timeout=10):
    """Fetch and extract text content from a website."""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Get text content
        text = soup.get_text()
        
        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        return text
        
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None
