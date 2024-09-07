import flet as ft



class Detect(ft.View):
    """ Detection view """

    def __init__(self):
        super().__init__()
        self.route = "/detect"
        self.controls = [ 

            ft.AppBar(title=ft.Text("Detect"), bgcolor=ft.colors.SURFACE_VARIANT),
            #ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),

            ft.Text(f"Spot the suspect:"),

            ft.Stack([c, gd1], width=1000, height=400),

            #ft.Text(f"Position: {control.top}"),

            ft.TextField(label="Describe the problem"),

            ft.TextButton("CONTINUE", on_click=lambda _: self.page.go("/improve"))
        ]

def on_pan_update1(e: ft.DragUpdateEvent):
    c.top = max(0, c.top + e.delta_y)
    c.left = max(0, c.left + e.delta_x)
    c.update()

def on_pan_update2(e: ft.DragUpdateEvent):
    e.control.top = max(0, e.control.top + e.delta_y)
    e.control.left = max(0, e.control.left + e.delta_x)
    e.control.update()

def gesture():
	return ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=10,
        on_vertical_drag_update=on_pan_update2,
        left=100,
        top=100,
        content=ft.Container(bgcolor=ft.colors.BLUE, width=50, height=50),
    )

def pick_files_result(e: ft.FilePickerResultEvent):
    selected_files.value = (
        ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
    )
    selected_files.update()

def filepicker():
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    return pick_files_dialog


gd1 = ft.GestureDetector(
    mouse_cursor=ft.MouseCursor.MOVE,
    drag_interval=50,
    on_pan_update=on_pan_update1,
)

c = ft.Container(gd1, bgcolor=ft.colors.AMBER, width=50, height=50, left=0, top=0)
