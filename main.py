import flet as ft


def main(page: ft.Page):
    page.title = "Wiglitcher"

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
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
        )
        if page.route == "/metadata":
            page.views.append(
                ft.View(
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
            )
        if page.route == "/detect":
            page.views.append(
                ft.View(
                    "/detect",
                    [#detect page
                        ft.AppBar(title=ft.Text("Detect"), bgcolor=ft.colors.SURFACE_VARIANT),
                        #ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),

                        ft.Text(f"Spot the suspect:"),


                    ],
                )
            )    
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


#buttons management
    def handle_close(e):
        page.close(dlg_hot)
        #page.add(ft.Text(f"Hot dialog closed with action: {e.control.text}"))


    dlg_hot = ft.AlertDialog(
        modal=True,
        title=ft.Text("Let's wiglitchi it!"),
        content=ft.Text("Do you want..."),
        actions=[
            ft.TextButton("help for using it with correct attribution?", on_click=handle_close),
            ft.TextButton("describe the problem and improve it?", on_click=handle_close),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: page.add(
            ft.Text("Hot dialog dismissed"),
        ),
    )





ft.app(main, view=ft.AppView.WEB_BROWSER)











