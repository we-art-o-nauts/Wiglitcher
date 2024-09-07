import datetime
import requests, json
import flet as ft

from pages import detect, improve, metadata

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

def main(page: ft.Page):
    page.title = "⋆ ◎ ✾ WIGLITCHER ✾ ◎ ⋆"
    page.bgcolor = ft.colors.TRANSPARENT
    page.adaptive = True

    def route_change(route):
        page.views.clear()
        page.views.append(pages.metadata.view())
        if page.route == "/metadata":
            page.views.append(pages.mm.view())
        if page.route == "/detect":
            page.views.append(pages.detect.view())
            
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


#dialog management
    def handle_close(e):
        page.close(dlg_hot)
        #page.add(ft.Text(f"Hot dialog closed with action: {e.control.text}"))


    dlg_hot = ft.AlertDialog(
        modal=True,
        title=ft.Text("Let's wiglitchi it!"),
        content=ft.Text("Do you want..."),
        actions=[
            ft.TextButton("help for using it with correct attribution?", on_click=handle_close),
            ft.TextButton("NEXT IMAGE", on_click=handle_close),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: page.add(
            ft.Text("Hot dialog dismissed"),
        ),
    )



ft.app(target=main) #, view=ft.AppView.WEB_BROWSER)
