# fase2.py - Agente Nova con google-genai

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Configuración: cambia aquí la personalidad del agente
MODELO = "gemini-3.6-flash"
PERSONALIDAD = """
Eres un asistente útil.
"""

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Falta GEMINI_API_KEY en el archivo .env")

client = genai.Client(api_key=api_key)

try:
    chat = client.chats.create(
        model=MODELO,
        config=types.GenerateContentConfig(system_instruction=PERSONALIDAD)
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