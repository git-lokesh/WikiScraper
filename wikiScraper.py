import requests
from bs4 import BeautifulSoup

WikiLink = input("Enter a Wikipedia article link: ").strip()

try:
    response = requests.get(WikiLink)
    response.raise_for_status()

    page = BeautifulSoup(response.text, "html.parser")

    store_data = input("Do you want to store the data in a text file? (y/n): ").strip().lower()

    if store_data == "y":
        filename = "extracted_paragraphs.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            for p in page.select('p'):
                paragraph_text = p.get_text().strip()
                if paragraph_text:
                    file.write(paragraph_text + "\n\n")
        print(f"\nData has been stored in {filename}")
    else:
        print("\n--- Extracted Paragraphs ---\n")
        for p in page.select('p'):
            paragraph_text = p.get_text().strip()
            if paragraph_text:
                print(paragraph_text, "\n")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
