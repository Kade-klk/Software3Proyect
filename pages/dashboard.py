from flet import *
from utils.extras import *

class DashboardPage(Container):
    def __init__(self, switch_page, email):
        super().__init__()

        # Define animación de desplazamiento
        self.offset = transform.Offset(0, 0)

        # Almacena el email del usuario
        self.email = email

        # Define función para cambiar de pantalla
        self.switch_page = switch_page

        # Hace que la página ocupe todo el espacio disponible
        self.expand = True

        # Contenido principal del Dashboard
        self.content = Container(
            height=BASE_HEIGHT,
            width=BASE_WIDTH,
            bgcolor=BASE_COLOR,
            clip_behavior=ClipBehavior.ANTI_ALIAS,  # Bordes más suaves
            expand=True,
            border_radius=BORDER_RADIUS,  # Bordes redondeados
            content=Column(
                vertical_alignment='center',  # Alineación vertical centrada
                horizontal_alignment='center',  # Alineación horizontal centrada
                controls=[
                    # Mensaje de bienvenida
                    Text(value='Hello!'),

                    # Muestra el email del usuario
                    Text(value=f'Your email is\n{self.email}'),

                    # Botón de cierre de sesión
                    Container(
                        on_click=self.switch_page,  # Llama a switch_page para cerrar sesión
                        data='logout',
                        height=50,
                        width=100,
                        border_radius=30,
                        bgcolor='white',
                        content=Icon(
                            icons.LOGOUT_OUTLINED,
                            color='black'
                        )
                    )
                ]
            )
        )
