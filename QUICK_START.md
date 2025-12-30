# Guía de Inicio Rápido

Esta guía te ayudará a poner en marcha el Ecosistema Médico Regenera360 en minutos.

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git
- (Opcional) Node.js 14+ para funcionalidades JavaScript

## Instalación Rápida

### 1. Clonar el Repositorio

```bash
git clone https://github.com/regenera360nes-pixel/Ecosistema-Regenera360Fenix.git
cd Ecosistema-Regenera360Fenix
```

### 2. Crear Entorno Virtual (Recomendado)

```bash
# En Linux/Mac
python3 -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno

```bash
cp .env.example .env
```

Edita el archivo `.env` con tus credenciales. Puedes comenzar con valores de prueba y agregar las credenciales reales más tarde.

### 5. Verificar Instalación

```bash
python main.py
```

Selecciona la opción 3 para ejecutar prueba de integraciones.

## Modos de Uso

### Modo 1: API REST (Recomendado)

Inicia el servidor API para acceder a todos los servicios:

```bash
python main.py
# Selecciona opción 1
```

O directamente:

```bash
python -m uvicorn src.api.main:app --reload
```

Accede a la documentación interactiva en:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Modo 2: Orquestador de Automatización

Para ejecutar automatizaciones programadas:

```bash
python main.py
# Selecciona opción 2
```

### Modo 3: Ejemplos

Explora los ejemplos en el directorio `examples/`:

```bash
# Ejemplo de WhatsApp
python examples/whatsapp_example.py

# Ejemplo de AI
python examples/ai_assistant_example.py

# Flujo completo
python examples/complete_workflow_example.py
```

## Configuración de Integraciones

### Configuración Mínima

Para empezar a probar, solo necesitas:

1. **GitHub Token** (gratis):
   - Ve a GitHub Settings → Developer settings → Personal access tokens
   - Crea un nuevo token con permisos de `repo`
   - Agrega a `.env`: `GITHUB_TOKEN=tu_token`

### Configuración Completa

Para funcionalidad completa, configura todas las integraciones:

#### Huggingface (IA)
```env
HUGGINGFACE_API_KEY=tu_api_key
```
Obtén gratis en: https://huggingface.co

#### Wix
```env
WIX_API_KEY=tu_api_key
WIX_SITE_ID=tu_site_id
```
Obtén en: https://dev.wix.com

#### Meta Ads
```env
META_ACCESS_TOKEN=tu_token
META_APP_ID=tu_app_id
META_APP_SECRET=tu_secret
```
Crea app en: https://developers.facebook.com

#### WhatsApp Business (Twilio)
```env
WHATSAPP_ACCOUNT_SID=tu_sid
WHATSAPP_AUTH_TOKEN=tu_token
WHATSAPP_PHONE_NUMBER=whatsapp:+1234567890
```
Obtén en: https://www.twilio.com

#### Google Business
```env
GOOGLE_APPLICATION_CREDENTIALS=ruta/a/credentials.json
```
Crea proyecto en: https://console.cloud.google.com

## Primeros Pasos

### 1. Probar la API

```bash
# Inicia el servidor
python -m uvicorn src.api.main:app --reload

# En otra terminal, prueba el endpoint de salud
curl http://localhost:8000/health
```

### 2. Hacer una Consulta AI

```bash
curl -X POST http://localhost:8000/ai/query \
  -H "Content-Type: application/json" \
  -d '{"query": "¿Qué es la hipertensión?", "max_length": 200}'
```

### 3. Ver Estadísticas de GitHub

```bash
curl http://localhost:8000/github/stats
```

## Solución de Problemas

### Error: ModuleNotFoundError

```bash
# Asegúrate de tener el entorno virtual activado
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Reinstala las dependencias
pip install -r requirements.txt
```

### Error: Cannot connect to API

Verifica que las credenciales en `.env` sean correctas.

### Error: Port already in use

Cambia el puerto en `config/settings.py` o usa:

```bash
python -m uvicorn src.api.main:app --port 8001
```

## Siguientes Pasos

1. **Explora la Documentación API**: http://localhost:8000/docs
2. **Lee el README**: Contiene información detallada
3. **Ejecuta los Ejemplos**: Directorio `examples/`
4. **Personaliza**: Adapta el código a tus necesidades

## Soporte

- **Issues**: https://github.com/regenera360nes-pixel/Ecosistema-Regenera360Fenix/issues
- **Documentación**: Ver README.md completo

## Recursos Adicionales

- [Documentación Completa](README.md)
- [Ejemplos de Uso](examples/README.md)
- [Configuración Avanzada](config/README.md)

---

¡Listo para transformar la atención médica con IA! 🏥✨
