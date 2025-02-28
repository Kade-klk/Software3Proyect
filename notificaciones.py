import flet as ft

def main(page: ft.Page):
    page.title = "Notifications"
    page.bgcolor = "#D3E8C8"  # Color de fondo similar al de la imagen

    # Título con flecha de regreso
    title = ft.Row(
        controls=[
            ft.Icon(ft.icons.ARROW_BACK),
            ft.Text("notifications", size=20, weight=ft.FontWeight.BOLD)
        ],
        alignment=ft.MainAxisAlignment.START
    )

    # Botones superiores
    buttons = ft.Row(
        controls=[
            ft.OutlinedButton(text="received (0)"),
            ft.OutlinedButton(text="waiting (0)"),
            ft.OutlinedButton(text="blocked (0)")
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Imagen de notificación vacía
    image = ft.Image(
        src="assets/images/empty_notifications.png",  # Ajusta la ruta
        width=200,
        height=200
    )

    # Mensaje de "No tienes notificaciones"
    no_notifications_text = ft.Text(
        "you don't have notifications",
        size=16,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    # Layout principal
    content = ft.Column(
        controls=[title, buttons, image, no_notifications_text],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(content)

ft.app(target=main)
