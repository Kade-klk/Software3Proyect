from flet import *
from utils.extras import *

class LoginPage(Container):
    def __init__(self, switch_page, name, email, dp):
        super().__init__()

        # Almacena datos del usuario
        self.name = name
        self.email = email
        self.dp_url = dp

        # Define animación de desplazamiento
        self.offset = transform.Offset(0, 0)

        # Define función para cambiar de pantalla
        self.switch_page = switch_page

        # Hace que la página ocupe todo el espacio disponible
        self.expand = True

        # Texto para mostrar/ocultar contraseña
        self.view_hide_text = Text(value='View', color=BASE_COLOR, font_family='poppins medium')

        # Campo de entrada de contraseña
        self.pwd_input = Container(
            height=BTN_HEIGHT,
            bgcolor='white',
            border_radius=10,
            content=TextField(
                on_focus=self.password_field_in_focus,
                password=True,  # Oculta la contraseña por defecto
                suffix=Container(
                    on_click=self.view_hide_password,  # Botón para ver/ocultar contraseña
                    content=self.view_hide_text,
                ),
                hint_text='Password',
                hint_style=TextStyle(size=16, font_family='Poppins Regular', color=INPUT_HINT_COLOR),
                text_style=TextStyle(size=16, font_family='Poppins Regular', color=INPUT_HINT_COLOR),
                border=InputBorder.NONE,
                content_padding=CONTENT_PADDING,
                selection_color=BASE_GREEN,
                cursor_color=BASE_COLOR
            )
        )

        # Mensaje de error cuando la contraseña es incorrecta
        self.error = Row(
            controls=[
                Image(src='assets/icons/danger.png'),
                Text(
                    value='Please enter the correct password to login',
                    color='red',
                    font_family='poppins regular'
                )
            ]
        )

        # Contenedor de datos del usuario y campo de contraseña
        self.login_box = Column(
            controls=[
                Row(
                    controls=[
                        Container(
                            height=50, width=50, bgcolor='white',
                            border_radius=25, image_fit=ImageFit.COVER,
                            image_src=self.dp_url
                        ),
                        Column(
                            spacing=0,
                            controls=[
                                Text(value=self.name, font_family='Poppins Semibold', size=14),
                                Text(value=self.email, font_family='Poppins light', size=14),
                            ]
                        )
                    ]
                ),
                Container(height=2),
                self.pwd_input,
                Container(height=1),

                # Botón de inicio de sesión
                Container(
                    data='login_clicked',
                    on_click=self.switch_page,
                    height=BTN_HEIGHT,
                    width=BTN_WIDTH,
                    bgcolor=BASE_GREEN,
                    border_radius=10,
                    alignment=alignment.center,
                    content=Text(value='Continue', font_family='Poppins Medium', size=16)
                ),
                Container(height=5),

                # Enlace para recuperar contraseña
                Container(
                    content=Text(
                        value='Forgot your password?',
                        size=14,
                        font_family='poppins medium',
                        color=BASE_GREEN
                    )
                ),
                Container(height=5)
            ]
        )

        # Contenido principal de la pantalla de inicio de sesión
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
                        content=Image(
                            src='assets/images/2.png',
                            scale=0.9
                        )
                    ),
                    # Contenedor de login
                    Container(
                        border_radius=BORDER_RADIUS,
                        height=BASE_HEIGHT,
                        width=BASE_WIDTH,
                        padding=padding.only(top=30, left=10, right=10),
                        content=Column(
                            controls=[
                                # Botón de regreso
                                Container(
                                    on_click=self.switch_page,
                                    data='main_page',
                                    content=Icon(
                                        icons.ARROW_BACK_IOS_OUTLINED,
                                        size=28
                                    )
                                ),
                                Container(height=160),

                                # Título "Login"
                                Container(
                                    margin=margin.only(left=20),
                                    content=Text(
                                        value='Login',
                                        font_family='Poppins Bold',
                                        size=30
                                    )
                                ),
                                Container(height=2),

                                # Caja de inicio de sesión con datos del usuario
                                Container(
                                    padding=20,
                                    bgcolor='#cc2d2b2c',
                                    border_radius=10,
                                    content=self.login_box
                                )
                            ]
                        )
                    )
                ]
            )
        )

    # Maneja la eliminación del mensaje de error cuando el campo de contraseña está en foco
    def password_field_in_focus(self, e):
        if self.error in self.login_box.controls:
            self.login_box.controls.remove(self.error)
            self.pwd_input.bgcolor = 'white'
            self.pwd_input.border = None
            self.pwd_input.update()
            self.login_box.update()

    # Cambia entre mostrar y ocultar la contraseña
    def view_hide_password(self, e):
        if self.pwd_input.content.password:
            self.pwd_input.content.password = False
            self.view_hide_text.value = 'Hide'
        else:
            self.view_hide_text.value = 'View'
            self.pwd_input.content.password = True
        self.pwd_input.content.update()
        self.view_hide_text.update()
