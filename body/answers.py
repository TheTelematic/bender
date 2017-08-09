from HTMLParser import HTMLParser
from BeautifulSoup import BeautifulSoup

import requests


class RandomAnswer(HTMLParser):
    @staticmethod
    def get():
        response = requests.get('http://random-answer.goodplace.eu/').text

        parsed_html = BeautifulSoup(response)
        return parsed_html.body.find('a', attrs={'href': 'http://random-answer.goodplace.eu', 'id': 'mylink'}).text\
            .replace('"', '')
