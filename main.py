import datetime
import requests, json
import flet as ft

from pages.home import Home
from pages.hotshot import Hotshot
from pages import metadata, improve, detect


def main(page: ft.Page):
    page.title = "⋆ ◎ ✾ WIGLITCHER ✾ ◎ ⋆"
    page.bgcolor = ft.colors.TRANSPARENT
    page.adaptive = True

    def route_change(route):
        page.views.clear()
        page.views.append(ft.View("/", [ Home() ]))
        if page.route == "/hotshot":
            page.views.append(ft.View("/hotshot", [ Hotshot() ]))
        if page.route == "/metadata":
            page.views.append(metadata.view(page))
        if page.route == "/detect":
            page.views.append(detect.view(page))
            
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main) #, view=ft.AppView.WEB_BROWSER)
