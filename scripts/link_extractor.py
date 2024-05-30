import requests
from bs4 import BeautifulSoup

def extract_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        links = soup.find_all('a')
        extracted_links = [link.get('href') for link in links]
        
        return extracted_links

    except Exception as e:
        print("Error:", e)
        return []


website_url = "http://testphp.vulnweb.com/"
links = extract_links(website_url)
for link in links:
    print(link)