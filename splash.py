import flet as ft

def splash_screen(page):
    header = ft.Text("Reinova", size=50, weight=ft.FontWeight.BOLD, color="black")
    subheader = ft.Text("A new way", size=20, italic=True, color="black")
    plant_image = ft.Image(
        src="https://github.com/Kade-klk/Software3Proyect/blob/main/assets/images/plant.png?raw=true",
        width=250,height=250)
    button = ft.ElevatedButton("Get Started",
        on_click=lambda e: page.go("/customers"),  # Navegar a la pantalla de clientes
        bgcolor="blue",
        color="white",
        width=250,
        height=70
    )

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

    return ft.View(
        route="/",
        bgcolor="#CBEAD3",  # Corregido para que el fondo sea verde claro
        controls=[
            ft.Container(
                content=content,
                alignment=ft.alignment.center,
                expand=True
            )
        ]
    )

ft.app(target=splash_screen)
