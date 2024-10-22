import requests
from bs4 import BeautifulSoup

def scrape():
    url = 'https://www.example.com'
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Safely extract elements with error handling
        title = soup.select_one('h1')
        text = soup.select_one('p')
        link = soup.select_one('a')

        print(title.text if title else "No <h1> found")
        print(text.text if text else "No <p> found")
        print(link.get('href') if link else "No <a> found")
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")

if __name__ == '__main__':
    scrape()