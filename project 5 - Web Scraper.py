import requests
from bs4 import BeautifulSoup
import csv

url = input("Enter the website URL: ").strip()
html_tag = input("Enter the HTML tag to scrape (e.g., h1, h2, h3, p): ").strip()

try:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        elements = soup.find_all(html_tag)

        with open('scraped_data.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Extracted Text'])
            for elem in elements:
                text = elem.get_text(strip=True)
                if text:
                    writer.writerow([text])
        print("Data scraped and saved to 'scraped_data.csv'.")


    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
except Exception as e:
    print(f"Error occurred: {e}")
