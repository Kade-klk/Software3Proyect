import flet as ft

def main(page: ft.Page):
    page.title = "Settings"
    page.bgcolor = "#D3E8C8"  # Color de fondo similar al de la imagen
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Botones de configuración
    buttons = [
        ft.ElevatedButton(text="profile settings", icon=ft.icons.PERSON_OUTLINE),
        ft.ElevatedButton(text="notification settings", icon=ft.icons.NOTIFICATIONS_OUTLINED),
        ft.ElevatedButton(text="app settings", icon=ft.icons.SETTINGS_OUTLINED),
        ft.ElevatedButton(text="night mode", icon=ft.icons.NIGHTLIGHT_ROUND),
        ft.ElevatedButton(text="log out", icon=ft.icons.EXIT_TO_APP),
    ]

    # Contenedor centrado
    content = ft.Column(
        controls=[
            ft.Row(
                [ft.Text("← settings", size=18)],
                alignment=ft.MainAxisAlignment.START
            ),
            ft.Column(
                buttons,
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            ft.Image(
                src="https://github.com/Kade-klk/Software3Proyect/blob/main/assets/images/settings_osito.png?raw=true",
                width=250,
                height=250
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(content)

ft.app(target=main)
