import flet as ft

def main(page: ft.Page):
    page.title = "Help & Support"
    page.bgcolor = "#CBEAD3"

    # Barra de búsqueda
    search_bar = ft.TextField(
        hint_text="Search question",
        expand=True,
        prefix_icon=ft.icons.SEARCH,
        bgcolor="#F4C2D7",
        border_radius=20
    )

    # Función para crear botones estilizados
    def create_button(text):
        return ft.Container(
            content=ft.Row(
                [ft.Text(text, weight="bold", color="black"), ft.Icon(ft.icons.ARROW_FORWARD, color="black")],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=15,
            bgcolor="#359286",
            border_radius=20,
            on_click=lambda e: print(f"Clicked: {text}"),
        )

    # Lista de botones
    buttons = [
        create_button("Chat with technical support"),
        create_button("Communication channels"),
        create_button("Problems with the UI"),
        create_button("Evaluate us"),
    ]

    # Contenedor principal centrado
    content_container = ft.Container(
        content=ft.Column(
            [
                ft.Text("Help & Support", size=20, weight="bold", color="black"),
                ft.Text("Hello! How can we help you?", size=16, weight="bold", color="black"),
                search_bar,
                *buttons,
                ft.Image(
                    src="https://github.com/Kade-klk/Software3Proyect/blob/main/assets/images/team.png?raw=true",
                    width=200
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centra verticalmente
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centra horizontalmente
        ),
        alignment=ft.alignment.center,  # Centra todo el contenedor en la página
        padding=20,
    )

    # Agregar el contenedor a la página
    page.add(content_container)

ft.app(target=main)
