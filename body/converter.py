import json

import requests
from eyes import print_warning

API_YOUTUBEINMP3 = 'http://www.youtubeinmp3.com/fetch/?format=JSON&video='


def youtube2mp3(urls_videos):

    url_audios = []

    for url in urls_videos:

        built_url = API_YOUTUBEINMP3 + url

        response = requests.post(url=built_url).text

        # print_warning(response)

        response = json.loads(response)

        url_audios.append({
            'title': response['title'],
            'link': response['link']
        })

    return url_audios
