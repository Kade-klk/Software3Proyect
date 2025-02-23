from flet import *
from utils.extras import *

class SignupPage(Container):
    def __init__(self, switch_page, email):
        super().__init__()

        # Atributos principales
        self.email = email
        self.switch_page = switch_page
        self.offset = transform.Offset(0, 0)
        self.expand = True

        # Campo de entrada para contraseña
        self.password_box = TextField(
            password=True,
            suffix=Container(
                on_click=lambda _: print('yeah'),
                content=Text(
                    value='View',
                    color=BASE_COLOR,
                    font_family='Poppins Medium',
                ),
            ),
            hint_text='Password',
            hint_style=TextStyle(size=16, font_family='Poppins Regular', color=INPUT_HINT_COLOR),
            text_style=TextStyle(size=16, font_family='Poppins Regular', color=INPUT_HINT_COLOR),
            border=InputBorder.NONE,
            content_padding=CONTENT_PADDING,
            selection_color=BASE_GREEN,
            cursor_color=BASE_COLOR,
        )

        # Campo de entrada para nombre
        self.name_box = TextField(
            hint_text='Name',
            hint_style=TextStyle(size=16, font_family='Poppins Regular', color=INPUT_HINT_COLOR),
            text_style=TextStyle(size=16, font_family='Poppins Regular', color=INPUT_HINT_COLOR),
            border=InputBorder.NONE,
            content_padding=CONTENT_PADDING,
        )

        # Mensaje de error
        self.error = Row(
            controls=[
                Image(src='assets/icons/danger.png'),
                Text(
                    value='Please check your email address.',
                    color='red',
                    font_family='Poppins Regular',
                ),
            ]
        )

        # Contenido principal de la página de registro
        self.content = Container(
            height=BASE_HEIGHT,
            width=BASE_WIDTH,
            bgcolor=BASE_COLOR,
            clip_behavior=ClipBehavior.ANTI_ALIAS,
            expand=True,
            border_radius=BORDER_RADIUS,
            content=Stack(
                controls=[
                    # Imagen decorativa de fondo
                    Container(
                        height=BASE_HEIGHT,
                        width=BASE_WIDTH,
                        left=60,
                        top=-200,
                        content=Image(src='assets/images/2.png', scale=0.9),
                    ),

                    # Contenedor principal con el formulario
                    Container(
                        border_radius=BORDER_RADIUS,
                        height=BASE_HEIGHT,
                        width=BASE_WIDTH,
                        padding=padding.only(top=30, left=10, right=10),
                        content=Column(
                            controls=[
                                # Botón de retroceso
                                Container(
                                    data='main_page',
                                    on_click=self.switch_page,
                                    content=Icon(icons.ARROW_BACK_IOS_OUTLINED, size=28),
                                ),

                                Container(height=160),

                                # Título de la página
                                Container(
                                    margin=margin.only(left=20),
                                    content=Text(value='Sign up', font_family='Poppins Bold', size=30),
                                ),

                                Container(height=2),

                                # Formulario de registro
                                Container(
                                    padding=20,
                                    bgcolor='#cc2d2b2c',
                                    border_radius=10,
                                    content=Column(
                                        controls=[
                                            # Mensaje de bienvenida
                                            Column(
                                                spacing=0,
                                                controls=[
                                                    Text(
                                                        value="Looks like you don't have an account.\nLet's create a new account for",
                                                        size=14,
                                                        font_family='Poppins Light',
                                                        color='#ccffffff',
                                                    ),
                                                    Text(
                                                        value=self.email,
                                                        size=14,
                                                        font_family='Poppins Medium',
                                                        color='#ccffffff',
                                                    ),
                                                ],
                                            ),

                                            Container(height=1),

                                            # Campo de entrada del nombre
                                            Container(
                                                height=BTN_HEIGHT,
                                                bgcolor='white',
                                                border_radius=10,
                                                content=self.name_box,
                                            ),

                                            Container(height=1),

                                            # Campo de entrada de la contraseña
                                            Container(
                                                height=BTN_HEIGHT,
                                                bgcolor='white',
                                                border_radius=10,
                                                content=self.password_box,
                                            ),

                                            Container(height=1),

                                            # Términos y condiciones
                                            Container(
                                                content=Column(
                                                    spacing=0,
                                                    controls=[
                                                        Text(
                                                            value="By clicking 'Agree and Continue' below,",
                                                            size=14,
                                                            font_family='Poppins Light',
                                                            color='#ccffffff',
                                                        ),
                                                        Row(
                                                            spacing=0,
                                                            controls=[
                                                                Text(
                                                                    value="I agree to ",
                                                                    size=14,
                                                                    font_family='Poppins Light',
                                                                    color='#ccffffff',
                                                                ),
                                                                Text(
                                                                    value="Terms of Service and Privacy Policy",
                                                                    size=14,
                                                                    font_family='Poppins Medium',
                                                                    color=BASE_GREEN,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ),

                                            Container(height=1),

                                            # Botón de registro
                                            Container(
                                                data='register',
                                                on_click=self.switch_page,
                                                height=BTN_HEIGHT,
                                                width=BTN_WIDTH,
                                                bgcolor=BASE_GREEN,
                                                border_radius=10,
                                                alignment=alignment.center,
                                                content=Text(
                                                    value='Agree and Continue',
                                                    font_family='Poppins Medium',
                                                    size=16,
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )
