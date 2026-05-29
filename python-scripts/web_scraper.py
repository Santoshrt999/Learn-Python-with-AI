"""
Web Scraper — Extract headlines from a webpage using BeautifulSoup
Usage: python web_scraper.py <url>   or run directly for the default URL
"""

import sys
import requests
from bs4 import BeautifulSoup

DEFAULT_URL = "https://www.nbcsports.com/nfl/super-bowl"


def scrape_headlines(url: str, tag: str = "h1") -> list[str]:
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    return [el.get_text(strip=True) for el in soup.find_all(tag) if el.get_text(strip=True)]


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
    print(f"Scraping: {url}\n")

    headlines = scrape_headlines(url)
    if headlines:
        for h in headlines:
            print(f"  • {h}")
    else:
        print("  No headlines found.")
