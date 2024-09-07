# Metadata page

import flet as ft

def view():
	return ft.View(
        "/improve",
        [#IMPROVE VIEW
            ft.AppBar(title=ft.Text("Improve"), bgcolor=ft.colors.SURFACE_VARIANT),
            #ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),

            ft.Text(f"Improve by AI: LINK"),

            ft.Text(f"Improve text clarity: LINK"),

            ft.Text(f"Improve by Cropping a detail: LINK"),

            ft.ElevatedButton("Pick files", icon=ft.icons.UPLOAD_FILE, on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=True)),

        ],
    )