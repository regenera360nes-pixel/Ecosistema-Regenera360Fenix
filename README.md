# 🏥 Ecosistema Regenera360Fenix

Ecosistema médico integrado con IA que automatiza y conecta múltiples plataformas para mejorar la atención médica y la gestión de pacientes.

## 🌟 Características Principales

### Integraciones Implementadas

1. **🤖 Huggingface AI**
   - Asistencia médica con IA
   - Análisis de texto médico
   - Generación de respuestas inteligentes
   - Modelo: BioGPT-Large especializado en medicina

2. **💻 GitHub**
   - Gestión de repositorio
   - Automatización de issues
   - Generación de reportes automáticos
   - Pull requests automatizados

3. **🌐 Wix**
   - Gestión de sitio web
   - Formularios de contacto
   - Sistema de reservas/citas
   - Gestión de blog médico

4. **📱 Meta Ads (Facebook/Instagram)**
   - Campañas publicitarias automatizadas
   - Análisis de rendimiento
   - Segmentación de audiencia
   - Optimización de presupuesto

5. **💬 WhatsApp Business**
   - Mensajería automatizada con pacientes
   - Recordatorios de citas
   - Consejos de salud diarios
   - Respuestas automáticas con IA

6. **🔍 Google Business**
   - Gestión de perfil de negocio
   - Publicaciones automáticas
   - Gestión de reseñas
   - Actualización de horarios

## 🚀 Instalación

### Requisitos Previos

- Python 3.8+
- Node.js 14+
- Git
- Cuentas en las plataformas a integrar

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/regenera360nes-pixel/Ecosistema-Regenera360Fenix.git
cd Ecosistema-Regenera360Fenix
```

2. **Instalar dependencias Python**
```bash
pip install -r requirements.txt
```

3. **Instalar dependencias Node.js**
```bash
npm install
```

4. **Configurar variables de entorno**
```bash
cp .env.example .env
# Editar .env con sus credenciales
```

## ⚙️ Configuración

### Variables de Entorno Requeridas

Edite el archivo `.env` con sus credenciales:

```env
# Huggingface
HUGGINGFACE_API_KEY=your_key
HUGGINGFACE_MODEL_ID=microsoft/BioGPT-Large

# GitHub
GITHUB_TOKEN=your_token
GITHUB_REPO_OWNER=regenera360nes-pixel
GITHUB_REPO_NAME=Ecosistema-Regenera360Fenix

# Wix
WIX_API_KEY=your_key
WIX_SITE_ID=your_site_id
WIX_ACCOUNT_ID=your_account_id

# Meta/Facebook Ads
META_ACCESS_TOKEN=your_token
META_APP_ID=your_app_id
META_APP_SECRET=your_secret
META_AD_ACCOUNT_ID=your_account_id

# WhatsApp Business (Twilio)
WHATSAPP_ACCOUNT_SID=your_sid
WHATSAPP_AUTH_TOKEN=your_token
WHATSAPP_PHONE_NUMBER=whatsapp:+1234567890

# Google Business
GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json
GOOGLE_BUSINESS_ACCOUNT_ID=your_account_id
GOOGLE_LOCATION_ID=your_location_id
```

### Obtener Credenciales

#### Huggingface
1. Crear cuenta en [Huggingface](https://huggingface.co)
2. Ir a Settings → Access Tokens
3. Crear nuevo token

#### GitHub
1. Ir a Settings → Developer settings → Personal access tokens
2. Generar nuevo token con permisos de repo

#### Wix
1. Crear cuenta en [Wix Developers](https://dev.wix.com)
2. Crear app y obtener API key

#### Meta Ads
1. Crear app en [Meta for Developers](https://developers.facebook.com)
2. Configurar Marketing API
3. Obtener access token

#### WhatsApp Business (Twilio)
1. Crear cuenta en [Twilio](https://www.twilio.com)
2. Activar WhatsApp Business API
3. Obtener credenciales

#### Google Business
1. Crear proyecto en [Google Cloud Console](https://console.cloud.google.com)
2. Activar Google Business Profile API
3. Descargar credenciales JSON

## 🎯 Uso

### Opción 1: Menú Interactivo

```bash
python main.py
```

Seleccione una opción:
1. Iniciar API REST (FastAPI)
2. Iniciar orquestador de automatización
3. Ejecutar prueba de integraciones
4. Salir

### Opción 2: API REST

Iniciar el servidor API:

```bash
python -m uvicorn src.api.main:app --host 0.0.0.0 --port 8000
```

Acceder a la documentación interactiva:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Opción 3: Orquestador de Automatización

```bash
python -c "from src.automation import MedicalEcosystemOrchestrator; MedicalEcosystemOrchestrator().run()"
```

## 📡 API Endpoints

### IA y Análisis
- `POST /ai/query` - Consultar IA médica
- `POST /ai/analyze` - Analizar texto médico

### WhatsApp
- `POST /whatsapp/send` - Enviar mensaje
- `POST /whatsapp/appointment-reminder` - Enviar recordatorio de cita

### Wix
- `GET /wix/site-info` - Info del sitio
- `GET /wix/contacts` - Contactos del formulario

### Meta Ads
- `GET /meta/campaigns` - Listar campañas
- `GET /meta/insights` - Obtener métricas

### Google Business
- `GET /google/location` - Info de ubicación
- `GET /google/insights` - Métricas del negocio

### GitHub
- `GET /github/stats` - Estadísticas del repo
- `GET /github/issues` - Listar issues

### Automatización
- `POST /automation/daily-tips` - Enviar consejos diarios
- `POST /automation/daily-report` - Generar reporte diario
- `POST /automation/patient-inquiry` - Manejar consulta de paciente

## 🤖 Automatización

El sistema incluye automatizaciones programadas:

### Tareas Diarias
- **09:00** - Enviar consejos de salud a pacientes
- **10:00** - Sincronizar citas entre plataformas
- **15:00** - Enviar recordatorios de citas
- **18:00** - Generar reporte diario

### Tareas Semanales
- **Lunes 08:00** - Actualizar campañas de marketing
- **Viernes 17:00** - Generar análisis semanal

## 📁 Estructura del Proyecto

```
Ecosistema-Regenera360Fenix/
├── src/
│   ├── api/                    # FastAPI REST API
│   │   ├── __init__.py
│   │   └── main.py
│   ├── integrations/           # Integraciones con plataformas
│   │   ├── __init__.py
│   │   ├── huggingface_integration.py
│   │   ├── github_integration.py
│   │   ├── wix_integration.py
│   │   ├── meta_ads_integration.py
│   │   ├── whatsapp_integration.py
│   │   └── google_business_integration.py
│   ├── automation/             # Orquestador de automatización
│   │   ├── __init__.py
│   │   └── orchestrator.py
│   ├── models/                 # Modelos de datos
│   │   ├── __init__.py
│   │   └── schemas.py
│   └── utils/                  # Utilidades
├── config/                     # Configuraciones
│   ├── README.md
│   └── settings.py
├── main.py                     # Punto de entrada principal
├── requirements.txt            # Dependencias Python
├── package.json                # Dependencias Node.js
├── .env.example               # Ejemplo de variables de entorno
├── .gitignore                 # Archivos ignorados por Git
└── README.md                  # Este archivo
```

## 🔒 Seguridad

- **Nunca** comitee archivos `.env` con credenciales reales
- Use variables de entorno para información sensible
- Mantenga sus tokens y API keys seguros
- Revise regularmente los permisos de acceso
- Use HTTPS en producción

## 🛠️ Desarrollo

### Agregar Nueva Integración

1. Crear nuevo archivo en `src/integrations/`
2. Implementar clase de integración
3. Agregar a `src/integrations/__init__.py`
4. Actualizar `orchestrator.py`
5. Agregar endpoints en `src/api/main.py`

### Pruebas

```bash
# Probar integraciones
python main.py
# Seleccionar opción 3

# Probar API
curl http://localhost:8000/health
```

## 📊 Modelos de Datos

- **Patient**: Información de pacientes
- **Appointment**: Citas médicas
- **HealthTip**: Consejos de salud
- **MarketingCampaign**: Campañas publicitarias
- **Message**: Mensajes enviados
- **AnalyticsReport**: Reportes de análisis

## 🤝 Contribución

1. Fork el repositorio
2. Crear rama de feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

## 📝 Licencia

MIT License - ver archivo LICENSE para detalles

## 👥 Autor

Regenera360 Team

## 📞 Soporte

Para soporte, crear un issue en GitHub o contactar a través de:
- GitHub Issues: https://github.com/regenera360nes-pixel/Ecosistema-Regenera360Fenix/issues

## 🎓 Recursos Adicionales

- [Documentación Huggingface](https://huggingface.co/docs)
- [GitHub API Docs](https://docs.github.com/en/rest)
- [Wix Developer Docs](https://dev.wix.com)
- [Meta Marketing API](https://developers.facebook.com/docs/marketing-apis)
- [Twilio WhatsApp API](https://www.twilio.com/docs/whatsapp)
- [Google Business Profile API](https://developers.google.com/my-business)

## 🔄 Actualizaciones

Ver [CHANGELOG.md](CHANGELOG.md) para historial de cambios.

---

**Regenera360** - Transformando la salud con tecnología e IA 🏥✨
