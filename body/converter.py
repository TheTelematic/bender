import requests
from eyes import print_warning

API_FIRST_STEP = 'http://api.convert2mp3.cc/check.php?v='
API_SECOND_STEP_1 = 'http://dl'
API_SECOND_STEP_2 = '.downloader.space/dl.php?id='


def get_id_video(url):
    return url.split('?v=')[1]


def youtube2mp3(urls_videos):
    url_audios = []

    for url in urls_videos:

        built_url = API_FIRST_STEP + get_id_video(url)

        response = requests.post(url=built_url).text

        splitted_response = response.split('|')
        if splitted_response[0] != 'OK':
            song = 'ERROR'
            link = 'ERROR'
        else:

            song = splitted_response[3]

            link = API_SECOND_STEP_1 + splitted_response[1] + API_SECOND_STEP_2 + splitted_response[2]

        url_audios.append({
            'title': song,
            'link': link
        })

    return url_audios
