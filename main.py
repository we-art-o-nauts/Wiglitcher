import flet as ft


def main(page: ft.Page):
    page.title = "Wiglitcher2"


    #gesture
    def on_pan_update1(e: ft.DragUpdateEvent):
        c.top = max(0, c.top + e.delta_y)
        c.left = max(0, c.left + e.delta_x)
        c.update()

    def on_pan_update2(e: ft.DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.delta_y)
        e.control.left = max(0, e.control.left + e.delta_x)
        e.control.update()

    gd = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=50,
        on_pan_update=on_pan_update1,
    )

    c = ft.Container(gd, bgcolor=ft.colors.AMBER, width=50, height=50, left=0, top=0)

    gd1 = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=10,
        on_vertical_drag_update=on_pan_update2,
        left=100,
        top=100,
        content=ft.Container(bgcolor=ft.colors.BLUE, width=50, height=50),
    )
        
    #

    #filepicker
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.overlay.append(pick_files_dialog)
    #


    #VIEWS


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
                    [#METADATA VIEW
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
                    [#DETECT VIEW
                        ft.AppBar(title=ft.Text("Detect"), bgcolor=ft.colors.SURFACE_VARIANT),
                        #ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),

                        ft.Text(f"Spot the suspect:"),

                        ft.Stack([c, gd1], width=1000, height=400),

                        #ft.Text(f"Position: {control.top}"),

                        ft.TextField(label="Describe the problem"),

                        ft.TextButton("CONTINUE", on_click=lambda _: page.go("/improve"))
                    ],
                )
            )

        if page.route == "/improve":
            page.views.append(
                ft.View(
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
            )
            
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


#dialog management
    def handle_close(e):
        page.close(dlg_hot)
        #page.add(ft.Text(f"Hot dialog closed with action: {e.control.text}"))


    dlg_hot = ft.AlertDialog(
        modal=True,
        title=ft.Text("Let's wiglitchi it!"),
        content=ft.Text("Do you want..."),
        actions=[
            ft.TextButton("help for using it with correct attribution?", on_click=handle_close),
            ft.TextButton("NEXT IMAGE", on_click=handle_close),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: page.add(
            ft.Text("Hot dialog dismissed"),
        ),
    )





ft.app(main, view=ft.AppView.WEB_BROWSER)











