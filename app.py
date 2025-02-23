from flet import *
import pickle
import asyncio
import os
from utils.extras import *
from pages.mainpage import MainPage
from pages.login import LoginPage
from pages.signup import SignupPage
from pages.dashboard import DashboardPage
from service.auth import get_user, authenticate, verify_token, register_user, is_valid_email


# Función para guardar el token de sesión en un archivo local
async def save_token(token):
    try:
        with open("token.pkl", "wb") as f:
            pickle.dump(token, f)
        return "Saved"
    except:
        return None


# Función para cargar el token de sesión almacenado
async def load_token():
    try:
        with open("token.pkl", "rb") as f:
            stored_token = pickle.load(f)
        return stored_token
    except:
        return None


# Clase que permite arrastrar la ventana de la aplicación
class WindowDrag(Control):
    def build(self):
        return Container(content=WindowDragArea(height=10, content=Container(bgcolor="white")))


# Clase principal de la aplicación
class App(Control):
    def __init__(self, pg: Page):
        super().__init__()

        # Configuración de la ventana
        pg.window_title_bar_hidden = True
        pg.window_frameless = True
        pg.window_title_bar_buttons_hidden = True
        pg.bgcolor = colors.TRANSPARENT
        pg.window_bgcolor = colors.TRANSPARENT

        # Cargar fuentes personalizadas
        pg.fonts = {
            "SF Pro Bold": "fonts/SFProText-Bold.ttf",
            "Poppins Regular": "fonts/poppins/Poppins-Regular.ttf",
        }

        # Definir tamaño de la ventana
        pg.window_width = BASE_WIDTH
        pg.window_height = BASE_HEIGHT

        # Intentar verificar el token de sesión almacenado
        auth = asyncio.run(verify_token(asyncio.run(load_token())))

        self.pg = pg
        self.pg.spacing = 0
        self.delay = 0.1
        self.anim = animation.Animation(300, AnimationCurve.EASE_IN_OUT_CUBIC)

        # Página principal
        self.main_page = MainPage(self.switch_page)

        # Definir vistas de la pantalla
        self.screen_views = Stack(
            expand=True,
            controls=[
                self.main_page if not auth else DashboardPage(self.switch_page, auth["email"]),
            ]
        )

        self.init_helper()

    # Método para cambiar entre las páginas de la aplicación
    def switch_page(self, e):
        if e.control.data == "register":
            # Registro de usuario
            name = self.signup_page.name_box.value
            password = self.signup_page.password_box.value
            email = self.main_page.email_input.content.value

            user = register_user(name, email, password)
            self.screen_views.controls.clear()
            self.screen_views.controls.append(DashboardPage(self.switch_page, email))
            self.screen_views.update()
            return

        elif e.control.data == "process_login":
            # Procesar el inicio de sesión
            email = self.main_page.email_input.content.value
            if is_valid_email(email):
                user = get_user(email)
                if user:
                    self._name = user[1]
                    self._email = user[2]
                    self.screen_views.controls.clear()
                    self.login_page = LoginPage(self.switch_page, name=self._name, email=self._email, dp="")
                    self.screen_views.controls.append(self.login_page)
                    self.screen_views.update()
                else:
                    self.screen_views.controls.clear()
                    self.signup_page = SignupPage(self.switch_page, email)
                    self.screen_views.controls.append(self.signup_page)
                    self.screen_views.update()
            else:
                # Mostrar error si el correo no es válido
                self.main_page.email_input.bgcolor = INPUT_ERROR_BG
                self.main_page.email_input.border = border.all(width=2, color=INPUT_ERROR_OUTLINE)
                self.main_page.main_content.controls.insert(1, self.main_page.error)
                self.main_page.update()

        elif e.control.data == "main_page":
            # Regresar a la página principal
            self.screen_views.controls.clear()
            self.screen_views.controls.append(self.main_page)
            self.screen_views.update()

        elif e.control.data == "login_clicked":
            # Autenticación del usuario
            password = self.login_page.pwd_input.content.value
            email = self.login_page.email
            auth = authenticate(email, password)

            if auth:
                asyncio.run(save_token(auth))
                self.screen_views.controls.clear()
                self.screen_views.controls.append(DashboardPage(self.switch_page, email))
                self.screen_views.update()
            else:
                # Mostrar error si las credenciales son incorrectas
                self.login_page.login_box.controls.insert(4, self.login_page.error)
                self.login_page.pwd_input.bgcolor = INPUT_ERROR_BG
                self.login_page.pwd_input.border = border.all(width=2, color=INPUT_ERROR_OUTLINE)
                self.login_page.pwd_input.update()
                self.login_page.login_box.update()

        elif e.control.data == "logout":
            # Cerrar sesión y eliminar el token almacenado
            try:
                os.remove("token.pkl")
            except:
                pass
            self.screen_views.controls.clear()
            self.screen_views.controls.append(self.main_page)
            self.screen_views.update()

    # Método para inicializar los elementos en la interfaz
    def init_helper(self):
        self.pg.add(
            WindowDrag(),
            self.screen_views
        )


# Iniciar la aplicación con la clase principal
app(target=App, assets_dir="assets")
