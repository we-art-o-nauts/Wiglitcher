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
  'Authorization': 'Bearer ' + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJkMzQ3MDIxZjY1MzQxZjA5ZmNlZmZlMzg4ODg3OGRjNSIsImp0aSI6IjNmMzA3MTA3N2ZlMTQ4ZmRkMjZkZGUxZTdlYzFjMjYxY2ZkNDc0MDMwNDkyNTA2ZWFmNzFlNjIxOGNiYTBlMDE0N2Y1ZGU2NzQ4NzhmNDQ3IiwiaWF0IjoxNzI1NzA0Mjg1LjUwMjkzNCwibmJmIjoxNzI1NzA0Mjg1LjUwMjkzNywiZXhwIjozMzI4MjYxMzA4NS41MDA4NTQsInN1YiI6IjIzNjk1IiwiaXNzIjoiaHR0cHM6Ly9tZXRhLndpa2ltZWRpYS5vcmciLCJyYXRlbGltaXQiOnsicmVxdWVzdHNfcGVyX3VuaXQiOjUwMDAsInVuaXQiOiJIT1VSIn0sInNjb3BlcyI6WyJiYXNpYyJdfQ.pl93T9l2c074X29oBnALveqUh2PWuptQ9C1udpqURqH3IEVPb917ckrxikw76yPmAJxeHVBODxygO1LPir7JEWwitVXP_pPnud_38BRaC35_ydIB0L7OKrfYg4hdVFPvqGW4NaLCsXd0QlsPE5qQhJpL-12czn1IMX74r3rGwoerD34sV7baCf1N3-my1MG6pw-g6xvLq2ZtwGlOLMDKvpjOEks77BxS-aYSJ9zT09Jjp2qWrqR9qKN33ZuZe3tbiPZygLrIYL8YLIGjbqmdcPQdzSbT7CnV9YgUuc-Nc9uh--7AS078rhEFw5Jm9CK_BWth7Ng7Gon-fl9Upy2JEbiBYUC1klGiM7VocwZX1MjwUF63AmMEvcwmbeN0Smb5EUhXhq6Xo9W8SNzb8vARxvVB631rVv5MQSD6cTSR5aX_KaipAYJU7hpwNq7cgurFkrdiEG8YW71dI3gxhEWnnHdFst1OaxWDu9Oa4pv8wDzqgTYMf8mbFou5T6jSGvnbasbHP3OwRLFpHd5jZ-8t87nlfy6iulwKptFASF7XkueYvc0DKWWaYlwNUiAiRjoXl4ARBlsVJos03WqiisTS8bFgeh9xCZ_UR7SNSUmkZG_s6Z6h1IcZW42Kb71PnfCSWaa-gvTsHMBdTYQfbibQwQyVUBlyxy7WmS9ap_Y1_Ak',
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

    def __init__(self, page):
        super().__init__()
        self.route = "/"
        self.page = page
        self.wiki_data = self.page.client_storage.get("wiki_data")
        self.controls = [ 

            ft.ListTile(
                leading=ft.Icon(ft.icons.ALBUM),
                title=ft.Text("WikiGlitcher"),
                subtitle=ft.Text(
                    "GLAMhack 2024 ~ zHB Luzern"
                ),
            ),

            ft.Column(self.column(self)) 
        ]

    def column(self, e):
        if self.wiki_data is None:
            self.wiki_data = get_todays_image()
            self.page.client_storage.set('wiki_data', self.wiki_data)

        return [
            ft.Image(
                src=self.wiki_data['thumbnail_url'],
                width=400,
                height=300,
                fit=ft.ImageFit.CONTAIN
            ),

            ft.Text(self.wiki_data['description_text']),

            ft.Text(f"Artist: " + self.wiki_data['artist_name']),
            ft.Text(f"License: " + self.wiki_data['license_name']),

            ft.Row(
                [
                    ft.TextButton("Hot", on_click=lambda e: self.page.go("/hotshot")), 
                    ft.TextButton("Not", on_click=lambda _: self.page.go("/detect"))
                ],
                #alignment=ft.MainAxisAlignment.CENTER,
            ),
        ]
