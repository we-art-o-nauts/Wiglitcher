# Metadata page

import flet as ft

def view():
	return ft.View(
                "/",
                [
                    ft.Card(
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

                                    ft.Image(src=f"C:\\first-flet-app\\TEST1\\images\\1.png",
                                    width=400,
                                    height=400,
                                    fit=ft.ImageFit.CONTAIN
                                    ),
                                    
                                    ft.Row(
                                        [ft.TextButton("METADATA", on_click=lambda _: page.go("/metadata"))],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),

                                    
                                    ft.Row(
                                        [ft.TextButton("Hot", on_click=lambda e: page.open(dlg_hot)), ft.TextButton("Not", on_click=lambda _: page.go("/detect"))],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),

                                    ft.Text(f"URL: "),

                                ]
                            ),
                            width=400,
                            padding=10,
                        )
                    )
                ],
            )

def mm():
    wiki_data = get_todays_image()
    print(wiki_data)
    return ft.View(
            "/metadata",
            [#metadata page
                ft.AppBar(title=ft.Text("Metadata"), bgcolor=ft.colors.SURFACE_VARIANT),
                #ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),

                ft.Text(f"Metadata:"),
                ft.Text(f"Name:"),
                ft.Text(f"Description:"),
                ft.Text(f"Date:"),
                ft.Text(f"Author:"),
                ft.Text(f"Author first edit:"),
                ft.Text(f"Author edit count:"),


            ],
        )
