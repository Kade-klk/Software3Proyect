import flet as ft

def main(page: ft.Page):
    page.title = "Reinova App"
    page.bgcolor = "#CBEAD3"

    header = ft.Text("Reinova", size=50, weight=ft.FontWeight.BOLD, color="black")
    subheader = ft.Text("A new way", size=20, italic=True, color="black")

    # Imagen agregada arriba del botón
    plant_image = ft.Image(
        src="https://github.com/Kade-klk/Software3Proyect/blob/main/Imagenes/plant.png?raw=true",
        width=250,
        height=250
    )

    button = ft.ElevatedButton(
        "Get Started",
        on_click=lambda e: print("Button clicked!"),
        bgcolor="blue",
        color="white",
        width=250,
        height=70
    )

    # Contenedor principal centrado
    content = ft.Column(
        [
            header,
            subheader,
            plant_image,
            button
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(
        ft.Container(
            content=content,
            alignment=ft.alignment.center,  # Centrar todo
            expand=True  # Ocupar todo el espacio de la pantalla
        )
    )

ft.app(target=main)
