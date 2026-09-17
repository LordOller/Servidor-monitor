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
