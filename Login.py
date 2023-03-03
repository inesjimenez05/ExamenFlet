import flet as ft


def main(page: ft.Page):

    def registro (e):
        nombre=tfnombre.value
        contraseña=tfpassword.value
        if nombre == contraseña:
            dlg = ft.AlertDialog(title=ft.Text("Contraseña y usuario correctos"), on_dismiss=lambda e: print("Dialog dismissed!"))
            page.dialog=dlg
            dlg.open = True
        page.update()

    page.title = "Examen Flet"

    page.horizontal_alignment= ft.CrossAxisAlignment.CENTER
    page.window_height=500
    page.window_width= 250

    img=ft.Image(src="fotos/Logo.png",width=100,height=100)
    page.update()
      
    tfnombre = ft.TextField(label="Nombre")
    tfpassword= ft.TextField(label="Contraseña",password=True, can_reveal_password=True)
    boton=ft.ElevatedButton("Registrarse", icon="add", on_click=registro)
    

    page.add(img,tfnombre,tfpassword,boton)
    

ft.app(target=main,assets_dir="fotos")