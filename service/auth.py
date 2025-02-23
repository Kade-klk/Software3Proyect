import firebase_admin
from firebase_admin import auth, credentials
import requests
import re
import os  # Para manejar variables de entorno

# Inicialización de Firebase con credenciales
cred = credentials.Certificate("service_account.json")
firebase_admin.initialize_app(cred)

# Carga la API Key desde una variable de entorno
API_KEY = os.getenv("FIREBASE_API_KEY")

def get_user(email):
    """
    Obtiene la información de un usuario de Firebase Authentication por su correo.
    Retorna una tupla con (uid, nombre, email) si el usuario existe, de lo contrario, devuelve None.
    """
    try:
        user = auth.get_user_by_email(email)
        return user.uid, user.display_name, user.email
    except auth.UserNotFoundError:
        print("Usuario no encontrado.")
        return None
    except Exception as e:
        print(f"Error al obtener usuario: {e}")
        return None

def register_user(name, email, password):
    """
    Registra un nuevo usuario en Firebase Authentication.
    Retorna el UID si se crea correctamente, de lo contrario, devuelve None.
    """
    if not is_valid_email(email):
        print("Correo electrónico no válido.")
        return None

    try:
        user = auth.create_user(
            email=email,
            password=password,
            display_name=name,
        )
        return user.uid
    except auth.EmailAlreadyExistsError:
        print("El correo ya está registrado.")
        return None
    except Exception as e:
        print(f"Error al registrar usuario: {e}")
        return None

def authenticate(email, password):
    """
    Autentica un usuario en Firebase usando email y contraseña.
    Retorna un token si las credenciales son correctas, de lo contrario, devuelve None.
    """
    if not API_KEY:
        print("Error: API Key de Firebase no encontrada.")
        return None

    auth_url = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={API_KEY}"

    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    try:
        response = requests.post(auth_url, json=payload)
        response_data = response.json()

        if response.status_code == 200:
            return response_data.get("idToken")  # Retorna el token si la autenticación es exitosa
        else:
            print(f"Error en autenticación: {response_data.get('error', {}).get('message', 'Desconocido')}")
            return None
    except requests.RequestException as e:
        print(f"Error en la solicitud de autenticación: {e}")
        return None

async def verify_token(token):
    """
    Verifica la validez de un token de Firebase Authentication.
    Retorna el token decodificado si es válido, de lo contrario, devuelve None.
    """
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except auth.InvalidIdTokenError:
        print("Token inválido.")
        return None
    except Exception as e:
        print(f"Error al verificar el token: {e}")
        return None

def is_valid_email(email):
    """
    Verifica si un email tiene un formato válido usando una expresión regular.
    Retorna True si el formato es válido, False en caso contrario.
    """
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None
