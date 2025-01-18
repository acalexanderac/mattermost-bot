import requests
from datetime import datetime

def main():
    url = "hook_url" #https://nes.partner.io/hooks/sanexsadtogeu1cyg234fgsafast1fuy
    
    # Obtener el día actual del mes
    current_day = datetime.now().day
    
    # Definir el mensaje según el día
    if current_day == 9:
        message = "📢 Recordatorio: El 9 Fecha límite para el nuevo feature ¡No lo olvides! 📢"
    elif current_day == 12:
        message = "🚨 ¡ÚLTIMO DÍA! Hoy es la fecha límite para el nuevo feature en producción 🚨"
    else:
        return

    body = {
        "channel": "channel_original_name",
        "username": "Name-Bot",
        "icon_url": "https://valorantinfo.com/images/us/bunny-hop-spray_valorant_gif_3789.gif",
        "text": message
    }

    r = requests.post(url, json=body)
    if r.status_code != 200:
        print(f"Error al enviar mensaje: {r.text}")

if __name__ == "__main__":
    main()

