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
        'description_html': jsondata['image']['description']['html'],
        'artist_name': jsondata['image']['artist']['text'],
        'attribution_url': jsondata['image']['file_page'],
        'license_name': jsondata['image']['license']['type'],
        'license_url': jsondata['image']['license']['url'],
    }

def view(page):
    """Wikimedia data page"""
    wiki_data = get_todays_image()
    #print(wiki_data)
    return ft.View(
            "/metadata",
            [
                ft.AppBar(title=ft.Text("Metadata"), bgcolor=ft.colors.SURFACE_VARIANT),

                ft.Image(
                    src=wiki_data['thumbnail_url'],
                    width=400,
                    height=300,
                    fit=ft.ImageFit.CONTAIN
                ),

                ft.Text(wiki_data['description_html']),

                ft.Text(f"Artist: " + wiki_data['artist_name']),
                ft.Text(f"License: " + wiki_data['license_name']),

            ],
        )
