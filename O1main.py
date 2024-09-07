import flet as ft


def main(page: ft.Page):


    page.update()






    page.add(ft.Text(f"Initial route: {page.route}"))

    def route_change(e: ft.RouteChangeEvent):
        page.add(ft.Text(f"New route: {e.route}"))

    def go_store(e):
        page.route = "/store"
        page.update()

    page.on_route_change = route_change








    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("WikiGlitch"),
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
                            [ft.TextButton("METADATA", on_click=go_store)],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),

                        
                        ft.Row(
                            [ft.TextButton("Hot", on_click=lambda e: page.open(dlg_modal)), ft.TextButton("Not")],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),


                    ]
                ),
                width=400,
                padding=10,
            )
        )
    )

    def handle_close(e):
        page.close(dlg_modal)
        page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))


    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("next step"),
        content=ft.Text("Do you want to use it?"),
        actions=[
            ft.TextButton("Yes", on_click=handle_close),
            ft.TextButton("No", on_click=handle_close),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: page.add(
            ft.Text("Modal dialog dismissed"),
        ),
    )


    
   
ft.app(main)
