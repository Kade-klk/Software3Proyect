import flet as ft
from flet.core.theme import Theme

def main(page: ft.Page):
    page.title = 'Lista de Ordenes'
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
        radius = 20,
    )

    tex2 = ft.Text('order list',
                   size = 40,
                   color = '#000000',
                   text_align = ft.TextAlign.CENTER,
    )

    r1 = ft.Row([ib, tex1, ca], alignment=ft.MainAxisAlignment.CENTER, spacing=10)

    lista_ordenes = ft.Column(scroll = ft.ScrollMode.AUTO,)
    # -------------------------- Prueba --------------------------------------------

    for i in range(10):
        p_item = f'item {i}'
        l_item = 'lote'
        d_item = 'direction'

        new_item = ft.ListTile(
            leading = ft.CircleAvatar(),
            title = ft.Text(f'{p_item}', color='#000000'),
            subtitle = ft.Text(f'{l_item}\n{d_item}',
                               color='#000000'
                               ),
            bgcolor = '#349287',
            trailing = ft.CupertinoButton(
            content=ft.Text('More Info'),
            on_click=lambda e: print('Mas informacion')
            )
        )
        lista_ordenes.controls.append(new_item)

    page.update()
    #--------------------------------------------------------------------------------

    btn1 = ft.CupertinoFilledButton(icon = ft.Icons.LIST,
                                    icon_color = '#000000',
                                    opacity_on_click=0.3,
                                    tooltip='Show more',
                                    on_click=lambda e: print("Show more clicked!"),
        )
    page.add(r1, tex2, lista_ordenes)


ft.app(target=main)