import json
import psutil
import requests

# Configuracion
discord_webhook_url = "https://discord.com/api/webhooks/1550189670590316717/FEsg_1lOqlzoPuH5r0woo8GwsIguZkePuiXXZJyt_kvSjP6mE27jmKOrEaajQjpiuDGM"
#Umbrales de alerta(En porcentaje)
umbral_cpu = 80.0
umbral_ram = 85.0
umbral_disco = 90.0

def enviarAlerta(mensaje):
    payload= { "content": f" 🚨**-----ALERTA DE SISTEMA**-----🚨 \n{mensaje}"}
    try:
         response = requests.post(discord_webhook_url, json=payload)
         response.raise_for_status()
    except Exception as e:
        print(f"Error al enviar alerta: {e}")

def revisar_salud_sistema():
    uso_cpu = psutil.cpu_percent(interval=1)
    uso_ram = psutil.virtual_memory().percent
    # Especificamos la unidad C: para Windows
    uso_disco = psutil.disk_usage("C:\\").percent

    alertas = []

    if uso_cpu > umbral_cpu:
        alertas.append(f"- **CPU alta:** {uso_cpu}% (Límite: {umbral_cpu}%)")

    if uso_ram > umbral_ram:
        alertas.append(f"- **RAM alta:** {uso_ram}% (Límite: {umbral_ram}%)")

    if uso_disco > umbral_disco:
        alertas.append(
            f"- **Disco C: casi lleno:** {uso_disco}% (Límite: {umbral_disco}%)"
        )

    if alertas:
        mensaje_final = "\n".join(alertas)
        enviarAlerta(mensaje_final)
    else:
        print(
            f"Sistema OK | CPU: {uso_cpu}% | RAM: {uso_ram}% | Disco C: {uso_disco}%"
        )


if __name__ == "__main__":
    revisar_salud_sistema()
