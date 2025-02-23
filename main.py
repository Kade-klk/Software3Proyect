import flet as ft

def main(page: ft.Page):
    page.title = "Reinova App"
    page.bgcolor = "#CBEAD3"

    header = ft.Text("Reinova", size=50, weight=ft.FontWeight.BOLD, color="black")
    subheader = ft.Text("A new way", size=20, italic=True, color="black")

    # Mostrar SVG en un IFrame
    svg_viewer = ft.IFrame(
        src="https://raw.githubusercontent.com/Kade-klk/Software3Proyect/3b8b0a184bee5a17f69a1a95c83dbd9b05fee9c7/Imagenes/plantphoto.svg",
        width=250,
        height=250
    )

    button = ft.ElevatedButton(
        "Get Started",
        on_click=lambda e: print("Button clicked!"),
        bgcolor="blue",
        color="white",
        width=250,
        height=70
    )

    container = ft.Column(
        [
            header, subheader,
            svg_viewer,  # Aquí va la imagen SVG
            button
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(container)

ft.app(target=main)
