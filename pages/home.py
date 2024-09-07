# Metadata page

import flet as ft
from os import path

class Home(ft.Row):
    def __init__(self):
        super().__init__()
        self.controls = [ self.card(self) ]

    def card(self, e):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [#main page
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("WikiGlitcher"),
                            subtitle=ft.Text(
                                "..."
                            ),
                        ),

                        ft.Image(
                            src=path.join("..", "images", "1.png"),
                            width=400,
                            height=400,
                            fit=ft.ImageFit.CONTAIN
                        ),
                        
                        ft.Row(
                            [ft.TextButton("METADATA", on_click=lambda _: self.page.go("/metadata"))],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),

                        
                        ft.Row(
                            [
                                ft.TextButton("Hot", on_click=lambda e: self.page.go("/hotshot")), 
                                ft.TextButton("Not", on_click=lambda _: self.page.go("/detect"))
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),

                        ft.Text(f"URL: "),

                    ]
                ),
                width=400,
                padding=10,
            )
        )

