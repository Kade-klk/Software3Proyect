import flet as ft

def customer_list(page):
    def add_customer(e):
        customer_list.controls.append(create_customer_item())
        page.update()

    def delete_customer(e):
        if customer_list.controls:
            customer_list.controls.pop()
            page.update()

    def create_customer_item():
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.CircleAvatar(content=ft.Icon(ft.icons.PERSON)),
                    ft.Column([
                        ft.Text("Name", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                        ft.Text("Age", color=ft.colors.BLACK),
                    ]),
                    ft.Text("Data", weight=ft.FontWeight.W_500, color=ft.colors.BLACK),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            padding=10,
            border_radius=10,
            bgcolor="white"
        )

    header = ft.Row([
        ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda e: page.go("/")),  # Regresar a la pantalla anterior
        ft.Text("Customers", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
        ft.CircleAvatar(content=ft.Icon(ft.icons.PERSON))
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    buttons = ft.Row([
        ft.Column([
            ft.IconButton(ft.icons.ADD, on_click=add_customer),
            ft.Text("Add Customer", color=ft.colors.BLACK)
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Column([
            ft.IconButton(ft.icons.REMOVE, on_click=delete_customer),
            ft.Text("Delete Customer", color=ft.colors.RED)
        ], alignment=ft.MainAxisAlignment.CENTER)
    ], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    customer_list = ft.Column()

    return ft.View(
        route="/customers",
        bgcolor="#CBEAD3",  # Corregido para que el fondo sea verde claro
        controls=[
            header,
            buttons,
            ft.Text("Customer List", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
            customer_list
        ]
    )
