import requests
from BeautifulSoup import BeautifulSoup


def get_new():
    url = 'https://hipertextual.com/'

    response = requests.post(url=url).text

    soup = BeautifulSoup(response)

    result = soup.find('a', {'class': 'linkPost--extended'})

    return result.get('href')

