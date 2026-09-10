# fase3.py - Agente Nova con herramientas (tool use)

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Configuración: cambia aquí la personalidad del agente
MODELO = "gemini-3.6-flash"
PERSONALIDAD = """
Eres Nova, un asistente técnico directo y sin rodeos.
Tienes una herramienta llamada leer_archivo que te permite leer archivos
del sistema. Úsala cuando el usuario te pida información sobre un archivo.
Si no sabes algo, di "No tengo esa información" en lugar de inventar.
Responde siempre en español.
"""

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Falta GEMINI_API_KEY en el archivo .env")

client = genai.Client(api_key=api_key)


# --- Herramienta que el agente puede usar ---
def leer_archivo(ruta: str) -> str:
    """Lee el contenido de un archivo de texto en la ruta especificada.

    Args:
        ruta: La ruta del archivo a leer.

    Returns:
        El contenido del archivo o un mensaje de error.
    """
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: el archivo '{ruta}' no existe."
    except Exception as e:
        return f"Error al leer el archivo: {e}"


try:
    chat = client.chats.create(
        model=MODELO,
        config=types.GenerateContentConfig(
            system_instruction=PERSONALIDAD,
            tools=[leer_archivo]
        )
    )

    while True:
        user_input = input("Tú: ")
        if user_input.strip().lower() == "salir":
            print("Nova: Hasta luego.")
            break

        response = chat.send_message(user_input)
        print(f"Nova: {response.text}")

except Exception as e:
    print(f"Error: {e}")