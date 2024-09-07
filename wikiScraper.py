import requests
from bs4 import BeautifulSoup

WikiLink = input("Enter a Wikipedia article link: ").strip()

try:
    response = requests.get(WikiLink)
    response.raise_for_status()

    page = BeautifulSoup(response.text, "html.parser")

    print("\n--- Extracted Paragraphs ---\n")
    for idx, p in enumerate(page.select('p'), start=1):
        paragraph_text = p.get_text().strip()
        if paragraph_text:
            print(f"{idx}. {paragraph_text}\n")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
