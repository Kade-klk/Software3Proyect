import flet as ft
from splash_screen import splash_screen
from customer_list import customer_list

def main(page: ft.Page):
    page.title = "Reinova App"
    page.bgcolor = "#CBEAD3"

    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(splash_screen(page))
        elif page.route == "/customers":
            page.views.append(customer_list(page))

        page.update()

    page.on_route_change = route_change
    page.go("/")  # Inicia en la pantalla de bienvenida

ft.app(target=main)
