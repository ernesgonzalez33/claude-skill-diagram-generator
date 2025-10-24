#!/usr/bin/env python3
"""
Single Page Parser - Extract and clean content from documentation pages

This script fetches a single webpage and extracts the main content,
removing navigation, sidebars, and other non-content elements.

Usage:
    python single_page_parser.py <url>
"""

import sys
import requests
from bs4 import BeautifulSoup
import re

def parse_page(url):
    """Main function to parse a documentation page"""
    print(f"Parsing: {url}")

    try:
        headers = {'User-Agent': 'Mozilla/5.0 (compatible; DocFlowGenerator/1.0)'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove navigation elements
        for element in soup.find_all(['nav', 'header', 'footer', 'aside']):
            element.decompose()

        # Extract main content
        main_content = soup.find('main') or soup.find('body')
        if main_content:
            content = main_content.get_text(separator='\n', strip=True)
            content = re.sub(r'\n\s*\n', '\n\n', content)

            return {
                'url': url,
                'content': content,
                'headings': [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
            }
    except Exception as e:
        print(f"Error parsing {url}: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python single_page_parser.py <url>")
        sys.exit(1)

    result = parse_page(sys.argv[1])
    if result:
        print(f"Successfully parsed {result['url']}")
        print(f"Content length: {len(result['content'])} characters")
        print(f"Found {len(result['headings'])} headings")
    else:
        print("Failed to parse page")