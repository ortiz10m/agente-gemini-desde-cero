# 🤖 Agente Gemini desde Cero

> Un agente de IA construido desde cero para aprender los fundamentos de los LLMs: llamadas a API, prompts de sistema y uso de herramientas (tool use).

**Por David Santiago Ortiz Rincón** · [@ortiz10m](https://github.com/ortiz10m)

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-API-4285F4?style=flat&logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

## 📖 Sobre el proyecto

Este repositorio documenta mi proceso de aprendizaje construyendo un agente de IA desde cero. No es un wrapper de una librería mágica: es código propio que entiende qué pasa por debajo.

El objetivo es entender los tres pilares de cualquier agente moderno:

1. **Llamadas a un LLM** — cómo enviar un prompt y recibir una respuesta vía API.
2. **Prompt de sistema** — cómo darle personalidad, reglas y límites al modelo.
3. **Tool Use** — cómo darle herramientas reales al agente para que ejecute acciones.

## 🗺️ Roadmap

- [x] **Fase 1** — Primera llamada a la API de Gemini
- [x] **Fase 2** — Prompt de sistema + personalidad
- [x] **Fase 3** — Tool use (agente que lee archivos)
- [x] **Fase 4** — Loop de agente completo
- [ ] **Fase 5** — Deploy / interfaz

## 🚀 Instalación

```bash
# 1. Clonar el repo
git clone https://github.com/ortiz10m/agente-gemini-desde-cero.git
cd agente-gemini-desde-cero

# 2. Crear entorno virtual
python -m venv venv

# 3. Activarlo
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Configurar la API key
# Crea un archivo .env con:
# GEMINI_API_KEY=tu_clave_aqui
```

## 🔑 Cómo obtener tu API key

1. Ve a [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Crea una API key gratuita (no pide tarjeta de crédito)
3. Pégala en tu archivo `.env` así:

```
GEMINI_API_KEY=tu_clave_aqui
```

## 💻 Uso

```bash
python fase1.py
python fase2.py
python fase3.py
python fase4.py
```

El agente final (`fase4.py`) incluye:

- **Reintentos automáticos** si el modelo falla por saturación (error 503).
- **Comandos especiales**: `/ayuda`, `/limpiar`.
- **Dos herramientas**: `leer_archivo` y `listar_archivos`.
- **Arquitectura modular** (config, herramientas y lógica separadas).

## 📁 Estructura del proyecto

```
agente-gemini-desde-cero/
├── agente/
│   ├── __init__.py       # Marca la carpeta como módulo Python
│   ├── config.py         # Configuración del agente (modelo, personalidad)
│   ├── herramientas.py   # Herramientas que el agente puede usar
│   └── agente.py         # Lógica del agente
├── fase1.py              # Primera llamada a Gemini
├── fase2.py              # Agente Nova con prompt de sistema
├── fase3.py              # Agente Nova con tool use
├── fase4.py              # Punto de entrada del agente modular
├── ver_modelos.py        # Lista los modelos disponibles en tu cuenta
├── requirements.txt      # Dependencias del proyecto
├── LICENSE               # Licencia MIT
├── .env                  # Tu API key (NO se sube a GitHub)
├── .gitignore            # Archivos ignorados por Git
└── README.md             # Este archivo
```

## 🛠️ Tecnologías

- **Python 3.10+**
- **google-genai** — SDK oficial de Google para Gemini
- **python-dotenv** — manejo de variables de entorno

## 📚 Lo que aprendí

- Cómo funciona una llamada a un LLM por debajo (auth → cliente → prompt → respuesta)
- Por qué los nombres de modelos caducan y cómo consultar los disponibles con `client.models.list()`
- Cómo un prompt de sistema define la personalidad completa de un agente
- Cómo darle herramientas a un agente para que ejecute acciones reales (tool use)
- Cómo separar un proyecto en módulos (config, herramientas, lógica)
- Cómo implementar reintentos automáticos ante errores de red
- Cómo añadir comandos especiales (`/ayuda`, `/limpiar`) al agente
- Buenas prácticas: nunca hardcodear API keys, usar `.gitignore`, separar dependencias en `requirements.txt`

## 🤝 Contribuciones

Este es un proyecto de aprendizaje personal, pero cualquier sugerencia es bienvenida vía issues.

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.
