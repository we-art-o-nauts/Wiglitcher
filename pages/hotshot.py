import flet as ft

class Hotshot(ft.View):
    """Hot shot views"""

    def __init__(self):
        super().__init__()
        self.route = "/hotshot"
        self.controls = [ 
            ft.AppBar(title=ft.Text("It's HOT!"), bgcolor=ft.colors.SURFACE_VARIANT),

            self.card(self) 
        ]

    def get_help(self):
        self.page.launch_url(
            'https://commons.wikimedia.org/wiki/Commons:Simple_media_reuse_guide',
            #web_window_name=ft.UrlTarget.BLANK
        )

    def next_image(self):
        #self.page.client_storage.set('wiki_data', False)
        self.page.go("/")

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
                                    on_click=lambda _: self.get_help()
                                ),
                                ft.TextButton(
                                    "NEXT IMAGE", 
                                    on_click=lambda _: self.next_image()
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

