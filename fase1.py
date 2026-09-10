import os
from dotenv import load_dotenv
from google import genai

# Cargar la API key desde el archivo .env
load_dotenv()

# Inicializar el cliente de Gemini
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Hacer una pregunta simple
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="¿Por qué el cielo es azul? Explícalo como si tuviera 10 años."
)

# Imprimir la respuesta
print(response.text)