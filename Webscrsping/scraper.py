import sys
import requests
from bs4 import BeautifulSoup


def scrape(url: str):
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "lxml")

    title = soup.title.string.strip() if soup.title and soup.title.string else "(no title)"
    headings = [h.get_text(strip=True) for h in soup.select("h1, h2")][:10]

    print(f"URL: {url}")
    print(f"Title: {title}")
    print("Headings:")
    for i, h in enumerate(headings, 1):
        print(f"  {i}. {h}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scraper.py <url>")
        raise SystemExit(1)
    scrape(sys.argv[1])
