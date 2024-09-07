# Metadata page

import flet as ft

class Hotshot(ft.Row):
    def __init__(self):
        super().__init__()
        self.controls = [ self.card(self) ]

    def card(self, e):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Let's wiglitchi it!"),
                        ft.Text("Do you want..."),
                        ft.Row(
                            [
                                ft.TextButton("help for using it with correct attribution?"),
                                ft.TextButton("NEXT IMAGE", on_click=lambda _: self.page.go("/metadata")),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )

