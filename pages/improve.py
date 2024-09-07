import flet as ft



def pick_files_result(e: ft.FilePickerResultEvent):
    selected_files.value = (
        ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
    )
    selected_files.update()

def filepicker():
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    return pick_files_dialog

class Improve(ft.View):
    """Improvement view"""

    def __init__(self):
        super().__init__()
        self.route = "/improve"
        self.controls = [ 

            ft.AppBar(title=ft.Text("Improve"), bgcolor=ft.colors.SURFACE_VARIANT),
            #ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),

            ft.Text(f"Improve RESOLUTION and DETAIL with AI: LINK"),

            ft.Text(f"Improve TEXT CLARITY with AI: LINK"),

            ft.Text(f"Improve by CROPPING the relavant regions: LINK"),

            ft.ElevatedButton(
                "UPLOAD TO COMMONS", 
                icon=ft.icons.UPLOAD_FILE, 
                on_click=lambda _: filepicker().pick_files(allow_multiple=True)),

        ]
 
