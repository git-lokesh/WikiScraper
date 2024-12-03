# Wikipedia Article Scraper

This Python script scrapes the paragraphs and links from a given Wikipedia article and allows the user to store them in text files.

## Prerequisites

- Python 3.x
- Install the following libraries using `pip`:
    - requests 
    - beautifulsoup4 or bs4

## Usage

1. Run the script.
2. Input a valid Wikipedia article link when prompted. For example: https://en.wikipedia.org/wiki/MS_Dhoni.
3. The script will ask whether you want to store the paragraphs and/or links in text files. You can choose y for yes or n for no.

## Sample Input

Enter a Wikipedia article link: https://en.wikipedia.org/wiki/MS_Dhoni

### Paragraph Storage

If you choose to store the paragraphs, the script will save the extracted paragraphs in a file named MS-Dhoni-paragraphs.txt.

### Links Storage

If you choose to store the links, the script will save all extracted links (URLs) in a file named MS-Dhoni-links.txt.

## Example Output

- MS-Dhoni-paragraphs.txt: Contains the textual content of all paragraphs from the article.
- MS-Dhoni-links.txt: Contains the URLs of all links from the article.

## Error Handling

If the script encounters an issue with the provided Wikipedia link (e.g., a network error), it will display an error message.

## License

This project is open-source and available under the MIT License.




**More data analytics and data cleaning will be added soon**

;)

