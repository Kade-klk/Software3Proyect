import flet as ft

def splash_screen(page: ft.Page):
    page.bgcolor = "#CBEAD3"
    page.title = "Reinova App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  #Centra todo
    Header =ft.Text( "Reinova", color = "Black")
    Sub_header = ft.Text( "a new way", color = "Black")
    plant_image = ft.Image(
        src="https://github.com/Kade-klk/Software3Proyect/blob/main/assets/images/plant.png?raw=true", width = 250, height=250)
    # def cambiar_pagina(e):

    botton =ft.FilledButton(text="Get Started")
    page.add(Header, Sub_header, plant_image,botton)


ft.app(target=splash_screen)
