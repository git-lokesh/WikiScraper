import requests
from bs4 import BeautifulSoup
import os

WikiLink = input("Enter a Wikipedia article link: ").strip()

try:
    response = requests.get(WikiLink)
    response.raise_for_status()

    page = BeautifulSoup(response.text, "html.parser")

    store_paragraphs = input("Do you want to store the paragraphs in a text file? (y/n): ").strip().lower()
    store_links = input("Do you want to store the links in a text file? (y/n): ").strip().lower()

    article_name = os.path.basename(WikiLink).replace('_', '-')

    if store_paragraphs == "y":
        paragraphs_filename = f"{article_name}-paragraphs.txt"
        with open(paragraphs_filename, 'w', encoding='utf-8') as paragraphs_file:
            for p in page.select('p'):
                paragraph_text = p.get_text().strip()
                if paragraph_text:
                    paragraphs_file.write(paragraph_text + "\n\n")
        print(f"\nParagraphs have been stored in {paragraphs_filename}")

    if store_links == "y":
        links_filename = f"{article_name}-links.txt"
        internal_wiki_links = []
        special_wiki_links = []
        external_links = []

        for a_tag in page.select('a[href]'):
            link = a_tag.get('href').strip()
            if link and not link.startswith('#'):
                if link.startswith("/wiki/"):
                    internal_wiki_links.append(link)
                elif link.startswith("/w/"):
                    special_wiki_links.append(link)
                elif link.startswith("http"):
                    external_links.append(link)

        with open(links_filename, 'w', encoding='utf-8') as links_file:
            # Writing Internal Wikipedia Links
            links_file.write("Internal Wikipedia Links (/wiki/):\n")
            for link in internal_wiki_links:
                links_file.write(f"https://en.wikipedia.org{link}\n")
            links_file.write("\n")

            # Writing Wikipedia Special Links
            links_file.write("Wikipedia Special Links (/w/):\n")
            for link in special_wiki_links:
                links_file.write(f"https://en.wikipedia.org{link}\n")
            links_file.write("\n")

            # Writing External Links
            links_file.write("External Links (http):\n")
            for link in external_links:
                links_file.write(f"{link}\n")

        print(f"Links have been stored in {links_filename}")

    if store_paragraphs != "y" and store_links != "y":
        print("\nNo data was saved.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
