import requests
from bs4 import BeautifulSoup
import csv

url = input("Enter the website URL: ").strip()

try:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)

        with open('scraped_data.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Full Page Text'])
            writer.writerow([text])

        print("Entire page text scraped and saved to 'scraped_data.csv'.")

    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")

except Exception as e:
    print(f"Error occurred: {e}")
