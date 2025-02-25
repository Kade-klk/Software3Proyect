import flet as ft

def main(page: ft.Page):
    page.title = "Customers"
    page.bgcolor = "#CBEAD3"
    page.window_width = 420
    page.window_height = 900

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
                        ft.Text("Name", weight=ft.FontWeight.BOLD),
                        ft.Text("Age"),
                    ]),
                    ft.Text("Data", weight=ft.FontWeight.W_500)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            padding=10,
            border_radius=10,
            bgcolor="white"
        )

    header = ft.Row([
        ft.IconButton(ft.icons.ARROW_BACK),
        ft.Text("Customers", size=20, weight=ft.FontWeight.BOLD),
        ft.CircleAvatar(content=ft.Icon(ft.icons.PERSON))
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    buttons = ft.Row([
        ft.Column([
            ft.IconButton(ft.icons.ADD, on_click=add_customer),
            ft.Text("Add Customer")
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Column([
            ft.IconButton(ft.icons.REMOVE, on_click=delete_customer),
            ft.Text("Delete Customer")
        ], alignment=ft.MainAxisAlignment.CENTER)
    ], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    customer_list = ft.Column()

    page.add(header, buttons, ft.Text("Customer List", size=16, weight=ft.FontWeight.BOLD), customer_list)

ft.app(target=main)
