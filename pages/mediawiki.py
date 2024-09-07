"""Utility class for Wikimedia API calls"""

import datetime
import requests, json

from dotenv import load_dotenv
from os import environ

load_dotenv()

today = datetime.datetime.now()
date = today.strftime('%Y/%m/%d')
language_code = 'en'

base_url = 'https://api.wikimedia.org/feed/v1/wikipedia/'
headers = {
  'Authorization': 'Bearer ' + environ.get('WIKIMEDIA_TOKEN'),
  'User-Agent': 'Wiglitcher (https://github.com/snappy91/Wiglitcher/issues)'
}

def get_todays_image():
    url = base_url + language_code + '/featured/' + date
    response = requests.get(url, headers=headers)
    jsondata = json.loads(response.text)
    if not 'image' in jsondata:
        print(jsondata)
        return None
    return {
        'thumbnail_url': jsondata['image']['thumbnail']['source'],
        'image_width': jsondata['image']['thumbnail']['width'],
        'image_height': jsondata['image']['thumbnail']['height'],
        'description_text': jsondata['image']['description']['text'],
        'artist_name': jsondata['image']['artist']['text'],
        'attribution_url': jsondata['image']['file_page'],
        'license_name': jsondata['image']['license']['type'],
        'license_url': jsondata['image']['license']['url'],
    }


base_url_random = 'https://commons.wikimedia.org/w/api.php?action=query&list=random&rnnamespace=6&format=json'
base_url_image = 'https://commons.wikimedia.org/w/api.php?action=query&prop=imageinfo&format=json'
def get_random_images(count=2):
    url = base_url_random + '&rnlimit=%d' % count
    response = requests.get(url, headers=headers)
    jsondata = json.loads(response.text)
    imagelist = '|'.join(img['title'] for img in jsondata['query']['random'])

    url2 = base_url_image + '&titles=' + imagelist + '&iilimit=50&iiprop=timestamp|user|url|size|thumbnailurl'
    response2 = requests.get(url2, headers=headers)
    imagedata = json.loads(response2.text)
    print(imagedata)

    idqp = imagedata['query']['pages']
    return [idqp[img]['imageinfo'] for img in idqp.keys()]

