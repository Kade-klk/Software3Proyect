from flet import *
from utils.extras import *

class MainPage(Container):
    def __init__(self, switch_page):
        super().__init__()

        # Define animación de desplazamiento
        self.offset = transform.Offset(0, 0)

        # Función para cambiar de pantalla
        self.switch_page = switch_page

        # Mensaje de error cuando el email es incorrecto
        self.error = Row(
            controls=[
                Image(src='assets/icons/danger.png'),
                Text(
                    value='Please check your email address.',
                    color='red',
                    font_family='poppins regular'
                )
            ]
        )

        # Hace que la página ocupe todo el espacio disponible
        self.expand = True

        # Campo de entrada de email
        self.email_input = Container(
            height=BTN_HEIGHT,
            bgcolor='white',
            border_radius=10,
            content=TextField(
                on_focus=self.field_in_focus,
                hint_text='Email',
                hint_style=TextStyle(size=16, font_family='Poppins Regular', color=INPUT_HINT_COLOR),
                text_style=TextStyle(size=16, font_family='Poppins Regular', color=INPUT_HINT_COLOR),
                border=InputBorder.NONE,
                content_padding=CONTENT_PADDING
            )
        )

        # Contenido principal con botones de login y opciones alternativas
        self.main_content = Column(
            controls=[
                self.email_input,
                Container(height=0),

                # Botón para continuar con el email
                Container(
                    on_click=self.switch_page,
                    data='process_login',
                    height=BTN_HEIGHT,
                    width=BTN_WIDTH,
                    bgcolor=BASE_GREEN,
                    border_radius=10,
                    alignment=alignment.center,
                    content=Text(value='Continue', font_family='Poppins Medium', size=18)
                ),

                # Separador "or"
                Row(
                    alignment='center',
                    controls=[Text(value='or', size=16, font_family='Poppins regular')]
                ),

                # Botón para continuar con Facebook
                Container(
                    height=BTN_HEIGHT,
                    width=BTN_WIDTH,
                    bgcolor=LIGHT_GREEN,
                    border_radius=10,
                    alignment=alignment.center,
                    padding=10,
                    content=Row(
                        controls=[
                            Image(src='assets/icons/facebook.png', scale=0.7),
                            Text(value='Continue with Facebook', font_family='Poppins semibold', size=18, color=BASE_COLOR),
                        ]
                    )
                ),

                Container(height=0),

                # Botón para continuar con Google
                Container(
                    height=BTN_HEIGHT,
                    width=BTN_WIDTH,
                    bgcolor=LIGHT_GREEN,
                    border_radius=10,
                    alignment=alignment.center,
                    padding=10,
                    content=Row(
                        controls=[
                            Image(src='assets/icons/google.png', scale=0.7),
                            Text(value='Continue with Google', font_family='Poppins semibold', size=18, color=BASE_COLOR),
                        ]
                    )
                ),

                Container(height=0),

                # Botón para continuar con Apple
                Container(
                    height=BTN_HEIGHT,
                    width=BTN_WIDTH,
                    bgcolor=LIGHT_GREEN,
                    border_radius=10,
                    alignment=alignment.center,
                    padding=10,
                    content=Row(
                        controls=[
                            Image(src='assets/icons/apple.png', scale=0.7),
                            Text(value='Continue with Apple', font_family='Poppins semibold', size=18, color=BASE_COLOR),
                        ]
                    )
                ),

                Container(height=20),

                # Enlace para recuperar contraseña
                Text(value='Forgot your password?', color=BASE_GREEN, size=16, font_family='Poppins Regular')
            ]
        )

        # Contenedor principal de la página
        self.content = Container(
            height=BASE_HEIGHT,
            width=BASE_WIDTH,
            bgcolor=BASE_COLOR,
            clip_behavior=ClipBehavior.ANTI_ALIAS,
            expand=True,
            border_radius=BORDER_RADIUS,
            content=Stack(
                controls=[
                    # Imagen de fondo
                    Container(
                        height=BASE_HEIGHT,
                        width=BASE_WIDTH,
                        left=60,
                        top=-200,
                        content=Image(src='assets/images/2.png', scale=0.9)
                    ),

                    # Contenedor de inicio de sesión
                    Container(
                        height=BASE_HEIGHT,
                        width=BASE_WIDTH,
                        padding=padding.only(top=30, left=10, right=10),
                        content=Column(
                            controls=[
                                Container(height=160),
                                Container(
                                    margin=margin.only(left=20),
                                    content=Text(value='Hi!', font_family='Poppins Bold', size=30)
                                ),
                                Container(height=2),
                                Container(
                                    padding=20,
                                    bgcolor='#cc2d2b2c',
                                    border_radius=10,
                                    content=self.main_content
                                )
                            ]
                        )
                    )
                ]
            )
        )

    # Maneja la eliminación del mensaje de error cuando el campo de email está en foco
    def field_in_focus(self, e):
        if self.error in self.main_content.controls:
            self.main_content.controls.remove(self.error)
            self.email_input.bgcolor = 'white'
            self.email_input.border = None
            self.main_content.update()
