# 🖥️ System Health Monitor & Discord Notifier

Un script ligero de automatización en **Python** diseñado para monitorear en tiempo real el estado de recursos críticos del sistema (CPU, Memoria RAM y almacenamiento en disco) y enviar alertas automáticas a **Discord** mediante Webhooks cuando se superan umbrales predefinidos.

Ideal para tareas de mantenimiento preventivo y monitoreo básico en entornos de soporte técnico, administración de sistemas y servidores.

---

## 🚀 Características

- **Monitoreo Multiplataforma:** Funciona tanto en **Windows** (unidad `C:`) como en **Linux** (`/`).
- **Alertas en Tiempo Real:** Integración con Discord mediante HTTP Webhooks en formato JSON.
- **Configuración de Umbrales:** Personalización de límites porcentuales para CPU, RAM y Disco.
- **Ejecución Desatendida:** Compatible con automatización mediante el **Programador de Tareas de Windows** o **Cron** en Linux.

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.x
- **Librerías:** 
  - `psutil` (Recolección de métricas del sistema)
  - `requests` (Consumo de APIs y envío de HTTP POST)
- **Integraciones:** Discord Webhooks

---

## 📋 Requisitos Previos

- Python 3.8 o superior instalado.
- Un servidor de Discord con un Webhook configurado.

---

## 🔧 Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TU-USUARIO/System-Health-Monitor.git](https://github.com/TU-USUARIO/System-Health-Monitor.git)
   cd System-Health-Monitor

2. **Crear y activar el entorno virtual:**

Windows:

PowerShell
python -m venv venv
.\venv\Scripts\activate
Linux/macOS:

Bash
python3 -m venv venv
source venv/bin/activate
2. **Instalar dependencias:**

Bash
pip install -r requirements.txt
Configurar el Webhook:
Abre el archivo monitor.py y reemplaza la variable DISCORD_WEBHOOK_URL con tu URL de Discord.

Ejecutar el script:

Bash
python monitor.py
###⚙️ Automatización
Para ejecutar el monitoreo de forma automática cada 15 minutos:

Windows: Configurar una tarea básica en el Programador de Tareas invocando el ejecutable de Python del entorno virtual (venv/Scripts/python.exe) apuntando a monitor.py.

Linux: Agregar la tarea a crontab -e:

Plaintext
*/15 * * * * /ruta/al/proyecto/venv/bin/python3 /ruta/al/proyecto/monitor.py

---

### Paso 3: Generar el archivo `requirements.txt`

Ejecuta este comando en la PowerShell (con el entorno virtual activado) para guardar las versiones de las librerías:

```powershell
pip freeze > requirements.txt
Paso 4: Subir todo a GitHub
Entra a GitHub.com y crea un Nuevo Repositorio (puedes llamarlo system-health-monitor). Déjalo Público y no desmarques las opciones de agregar README o gitignore (ya los creamos localmente).

Abre la consola en tu carpeta monitor-servidor y ejecuta comando por comando:

PowerShell
# Inicializar el repositorio Git local
git init

# Agregar todos los archivos
git add .

# Guardar el primer commit
git commit -m "feat: primer commit con monitor de salud de sistema y notificaciones a Discord"

# Renombrar la rama principal a main
git branch -M main

# Vincular con tu repositorio de GitHub (reemplaza con la URL de tu repo)
git remote add origin https://github.com/TU-USUARIO/system-health-monitor.git

# Subir el código
git push -u origin main
