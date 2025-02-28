import flet as ft
from flet.core.theme import Theme


def main(page: ft.Page):
    page.title = 'inventario'
    page.bgcolor = '#caead3'
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme = Theme(color_scheme_seed=ft.Colors.GREEN)



    ib = ft.IconButton(
        icon = ft.Icons.EXIT_TO_APP,
        icon_color = '#000000',
        icon_size = 30,
        tooltip = 'Salida',
    )

    tex1 =ft.Text('Inventario',
                  size = 30,
                  color = '#000000'
    )

    ca = ft.CircleAvatar(
        foreground_image_src='https://www.iconpacks.net/free-icon/user-3296.html',
        radius = 20,
    )

    tex2 = ft.Text('Your Inventory',
                   size = 40,
                   color = '#000000',
                   text_align = ft.TextAlign.CENTER,
    )

    lista = ft.Column(scroll=ft.ScrollMode.AUTO, )

    #---------------------Funcion de  Prueba------------------------
    def add_item(e):
        n_item = 'Nombre item'
        t_item = 'Tipo item'
        d_item = 'Desccripcion item'
        p_item = 'Precio item'
        new_item = ft.ListTile(
            leading = ft.CircleAvatar(),
            title=ft.Text(f'{n_item}', color='#000000'),
            subtitle=ft.Text(f'{t_item}\n{d_item}',
                             color='#000000'
                             ),
            bgcolor = '#349287',
            trailing = ft.Text(f'{p_item}', color='#000000'),
        )
        lista.controls.append(new_item)
        page.update()
        print('Añadido')
    #---------------------------------------------------------------------------

    ib1= ft.IconButton(
        icon = ft.Icons.ADD,
        icon_color = '#000000',
        icon_size = 30,
        tooltip = 'Añadir',
        style = ft.ButtonStyle(
            color = {ft.ControlState.DEFAULT: '#349287'},
            side = {ft.ControlState.DEFAULT: ft.BorderSide(2, '#349287')},
            shape=ft.CircleBorder(),
        ),
        on_click = add_item,
    )

    ib2=ft.IconButton(
        icon=ft.Icons.DELETE,
        icon_color='#000000',
        icon_size=30,
        tooltip='Eliminar',
        style=ft.ButtonStyle(
            color={ft.ControlState.DEFAULT: '#349287'},
            side={ft.ControlState.DEFAULT: ft.BorderSide(2, '#349287')},
            shape=ft.CircleBorder(),
        )
    )

    ib3= ft.IconButton(
        icon=ft.Icons.EDIT_NOTE,
        icon_color='#000000',
        icon_size=30,
        tooltip='Editar',
        style=ft.ButtonStyle(
            color={ft.ControlState.DEFAULT: '#349287'},
            side={ft.ControlState.DEFAULT: ft.BorderSide(2, '#349287')},
            shape=ft.CircleBorder(),
        )
    )

    r1 = ft.Row([ib, tex1, ca], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
    r2 = ft.Row([ib1, ib2, ib3], alignment=ft.MainAxisAlignment.CENTER, spacing=10)



    btn1 = ft.CupertinoFilledButton(icon = ft.Icons.LIST,
                                    icon_color = '#000000',
                                    opacity_on_click=0.3,
                                    tooltip='Show more',
                                    on_click=lambda e: print("Show more clicked!"),
        )
    page.add(r1, tex2, r2, lista, btn1)


ft.app(target=main)