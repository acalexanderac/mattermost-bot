# 🤖 Mattermost Bot Automatizado

¡Bienvenido a nuestra colección de bots para Mattermost! Estos bots están diseñados para ejecutarse diariamente y automatizar notificaciones importantes.

## 🌟 Características

- ⏰ Ejecución automática diaria
- 🔄 Integración perfecta con Mattermost
- 🛠 Fácil configuración
- 🚀 Ligero y eficiente
- 📅 Múltiples bots para diferentes necesidades

## 📋 Bots Disponibles

### 1. Bot Principal (`bot.py`)
Bot especializado en recordatorios de fechas límite para features:
- Envía recordatorio el día 9 de cada mes
- Envía alerta final el día 12 de cada mes
- Usa GIF personalizado como icono
- Canal y nombre de bot configurables

### 2. Bot Básico (`basic-bot.py`)
Bot simple para mensajes personalizados:
- Envía un mensaje personalizado al canal
- Usa un icono estático personalizado
- Ideal para mensajes únicos o pruebas

## 📋 Requisitos Previos

- Python 3.x
- Acceso a un servidor Mattermost
- Webhook URL configurado en Mattermost
- Permisos para ejecutar crontab en el servidor

## 🔧 Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/acalexanderac/mattermost-bot.git
cd mattermost-bot
```

2. Instala las dependencias necesarias:

```bash
pip install requests
```

3. Configura los webhooks en Mattermost:

- Abre el panel de administración de Mattermost
- Crea un nuevo webhook para cada bot
- Configura el nombre del canal y el icono
- Copia la URL del webhook para cada bot

4. Configura los bots:
- Reemplaza "hook_url" con tu URL de webhook en cada bot
- Modifica "channel_original_name" con tu canal
- Personaliza los nombres y iconos de los bots según necesites

## 🚀 Uso

### Bot Principal (bot.py)
- Se ejecuta diariamente y envía mensajes específicos:
  - Día 9: "📢 Recordatorio: El 9 Fecha límite para el nuevo feature ¡No lo olvides! 📢"
  - Día 12: "🚨 ¡ÚLTIMO DÍA! Hoy es la fecha límite para el nuevo feature en producción 🚨"

### Bot Básico (basic-bot.py)
- Envía un mensaje personalizado configurable
- Ideal para:
  - Pruebas de integración
  - Mensajes únicos
  - Notificaciones simples

### Personalización
- Puedes modificar los mensajes editando directamente los archivos
- Los iconos son personalizables vía `icon_url`
- El nombre del bot y canal son configurables en cada script

## 📋 Archivos Principales

- `bot.py`: Bot principal para recordatorios automáticos de fechas límite (días 9 y 12)
- `basic-bot.py`: Bot básico para enviar mensajes personalizados únicos
- `requirements.txt`: Lista de dependencias del proyecto

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Si tienes alguna idea para mejorar estos bots:

1. Haz fork del repositorio
2. Crea una nueva rama (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - mira el archivo `LICENSE` para más detalles.

## 📞 Contacto

[Alexander Arias](https://github.com/acalexanderac)  - acalexander774@gmail.com

Link del proyecto: [https://github.com/acalexanderac/mattermost-bot](https://github.com/acalexanderac/mattermost-bot)

## ⚙️ Configuración del Crontab

1. Abre el editor de crontab:

```bash
crontab -e
```

2. Configura la ejecución de los bots:

Para el bot principal (ejecutar diariamente a medianoche):
```bash
0 0 * * * /usr/bin/python3 /ruta/a/tu/bot.py
```

Para el bot básico (ejemplo: ejecutar cada lunes a las 9 AM):
```bash
0 9 * * 1 /usr/bin/python3 /ruta/a/tu/basic-bot.py
```

---
⌨️ con ❤️ por [Alexander Arias](https://github.com/acalexanderac)