# Metadata page

import flet as ft

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


class Metadata(ft.View):
    """Wikimedia data page"""

    def __init__(self):
        super().__init__()
        self.route = "/metadata"
        self.controls = [ 
            ft.AppBar(title=ft.Text("Metadata"), bgcolor=ft.colors.SURFACE_VARIANT),

            ft.Column(self.column(self)) 
        ]
    def column(self, e):
        wiki_data = get_todays_image()
        #print(wiki_data)
        return [
            ft.Image(
                src=wiki_data['thumbnail_url'],
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN
            ),

            ft.Text(wiki_data['description_text']),

            ft.Text(f"Artist: " + wiki_data['artist_name']),
            ft.Text(f"License: " + wiki_data['license_name']),
        ]
