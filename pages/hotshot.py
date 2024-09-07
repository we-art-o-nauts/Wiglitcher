# Metadata page

import flet as ft

class Hotshot(ft.View):
    def __init__(self):
        super().__init__()
        self.route = "/hotshot"
        self.controls = [ self.card(self) ]

    def get_help(self):
        pass
        #self.page.launch_url(
        #    'https://commons.wikimedia.org/wiki/Commons:Simple_media_reuse_guide',
        #    web_window_name=ft.UrlTarget.BLANK
        #)

    def card(self, e):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Let's wiglitchi it!"),
                        ft.Text("Do you want..."),
                        ft.Row(
                            [
                                ft.OutlinedButton(
                                    "Help me to use it correctly",
                                    on_click=self.get_help()
                                ),
                                ft.TextButton(
                                    "NEXT IMAGE", 
                                    on_click=lambda _: self.page.go("/metadata")
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )

