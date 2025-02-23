import flet as ft

def main(page: ft.Page):
    page.title = "Reinova App"
    page.bgcolor = "#CBEAD3"

    header = ft.Text(
        "Reinova",
        size=50,
        weight=ft.FontWeight.BOLD,
        color="black"
    )

    subheader = ft.Text(
        "A new way",
        size=20,
        italic=True,
        color="black"
    )

    # Imagen centrada (puedes cambiar la URL o usar una imagen local en "assets/")
    image = ft.Image(
        src="my-app\\Imagenes\\undraw_farming_u62j.png",  # Reemplaza con una URL real
        width=200,
        height=200
    )

    # Botón "Get Started"
    button = ft.ElevatedButton(
        "Get Started",
        on_click=lambda e: print("Button clicked!"),  # Puedes redirigir aquí a otra página
        bgcolor="blue",
        color="white",
        width=200,
        height=60,
    )

    # Contenedor principal con alineación en la parte superior
    container = ft.Column(
        [
            ft.Container(
                content=ft.Column(
                    [header, subheader],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                alignment=ft.alignment.top_center,
                padding=ft.padding.only(top=50),  # Ajuste mejorado sin valores negativos
            ),
            ft.Container(
                content=ft.Column(
                    [image, button],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                alignment=ft.alignment.center,
                expand=True
            )
        ]
    )

    # Agregar al page
    page.add(container)

ft.app(target=main)
