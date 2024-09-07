# Metadata page

import flet as ft

def view():
	return ft.View(
            "/detect",
            [#detect page
                ft.AppBar(title=ft.Text("Detect"), bgcolor=ft.colors.SURFACE_VARIANT),
                #ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),

                ft.Text(f"Spot the suspect:"),


            ],
        )
