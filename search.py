import flet as ft

def search(page: ft.Page):
    page.bgcolor = "#D3F0D0"
    page.title = "Reinova"
    page.padding = 20
    page.window_width = 800
    page.window_height = 600
    page.window_resizable = False
    page.window_maximizable = False
    page.window_minimizable = True
    page.window_title_bar_hidden = False

    def open_drawer(e):
        page.drawer.open = True
        page.update()

    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Column(
                controls=[
                    ft.Container(
                        padding=10,
                        content=ft.Column(
                            controls=[
                                ft.CircleAvatar(content=ft.Image(src="https://via.placeholder.com/100", width=50, height=50, fit=ft.ImageFit.CONTAIN), radius=25),
                                ft.TextField(label="Buscar", bgcolor="white", border_radius=25, width=250, height=40),
                                ft.Divider(),
                                ft.ListTile(leading=ft.Icon(ft.Icons.DASHBOARD, size=14), title=ft.Text("Panel")),
                                ft.ListTile(leading=ft.Icon(ft.Icons.SHOPPING_CART, size=14), title=ft.Text("Pedidos")),
                                ft.ListTile(leading=ft.Icon(ft.Icons.INVENTORY, size=14), title=ft.Text("Inventario")),
                                ft.ListTile(leading=ft.Icon(ft.Icons.PAYMENT, size=14), title=ft.Text("Pagos")),
                                ft.ListTile(leading=ft.Icon(ft.Icons.PEOPLE, size=14), title=ft.Text("Clientes")),
                                ft.Divider(),
                                ft.ListTile(leading=ft.Icon(ft.Icons.NOTIFICATIONS, size=14), title=ft.Text("Notificaciones")),
                                ft.ListTile(leading=ft.Icon(ft.Icons.HELP, size=14), title=ft.Text("Ayuda y Soporte")),
                                ft.ListTile(leading=ft.Icon(ft.Icons.SETTINGS, size=14), title=ft.Text("Configuraciones")),
                            ]
                        ),
                    )
                ]
            )
        ]
    )

    header = ft.Column(
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.IconButton(icon=ft.Icons.MENU, on_click=open_drawer, icon_size=18),
                    ft.Text("Reinova", size=20, weight=ft.FontWeight.BOLD),
                    ft.IconButton(icon=ft.Icons.PERSON, on_click=open_drawer, icon_size=18)
                ]
            ),
            ft.Container(
                content=ft.Image(
                    src="https://via.placeholder.com/150",
                    width=150,
                    height=150,
                    fit=ft.ImageFit.CONTAIN
                ),
                alignment=ft.alignment.center
            )
        ]
    )

    search_bar = ft.Container(
        content=ft.TextField(hint_text="Buscar", bgcolor="white", border_radius=25, width=250, height=40),
        alignment=ft.alignment.center,
        padding=10
    )

    icon_urls = [
        "https://via.placeholder.com/40", "https://via.placeholder.com/40",
        "https://via.placeholder.com/40", "https://via.placeholder.com/40",
        "https://via.placeholder.com/40", "https://via.placeholder.com/40",
        "https://via.placeholder.com/40", "https://via.placeholder.com/40"
    ]

    items_grid = ft.Container(
        content=ft.GridView(
            runs_count=4,
            child_aspect_ratio=1,
            spacing=5,
            controls=[
                ft.Container(
                    content=ft.Image(src=icon_urls[i], width=40, height=40, fit=ft.ImageFit.CONTAIN),
                    bgcolor="#A0D7A0",
                    width=40,
                    height=40,
                    border_radius=5
                ) for i in range(8)
            ]
        ),
        width=400,
        height=200,
        alignment=ft.alignment.center
    )

    page.add(
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                header,
                search_bar,
                ft.Container(content=items_grid, padding=10, alignment=ft.alignment.center)
            ]
        )
    )


ft.app(target=search, view=ft.FLET_APP)
