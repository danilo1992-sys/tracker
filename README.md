# Tracker  
![Version](https://img.shields.io/badge/version-0.1.0-blue)  

Tracker es una pequeña aplicación de línea de comandos escrita en **Python 3.14+** que permite a los usuarios:
- **Analizar un número de móvil**: obtiene la forma internacional, nacional, país, operador, ubicación, zona horaria y tipo de línea.
- **Rastrear una dirección IP**: devuelve país, región, ciudad, latitud, longitud, código postal, etc.
- **Mostrar la IP pública del equipo**: consulta el servicio `ipify` y la muestra de forma legible.

La cli está construida con `InquirerPy` para prompts interactivos, `phonenumbers` para la gestión de teléfonos, `tabulate` para tablas atractivas y `pyfiglet` para el banner inicial.

---

## 📖 Descripción

```
                         TRACER
```

Al arrancar se muestra un banner con el nombre *Tracker* y un menú desplegable con las opciones disponibles. Al elegir una, se solicita el dato necesario y se muestra la información resultante en tablas formateadas.

- **Numero de celular**:  
  - Verifica validez y posibilidad del número.  
  - Proporciona datos como formato E164, número nacional, región, operador, ubicación y zonas horarias.
- **Rastrear ip**:  
  - Pide una IP y consulta el API `https://ipwho.is`.  
  - Devuelve la geolocalización completa.
- **Cual es mi ip**:  
  - Hace una petición al API `https://api.ipify.org?format=json` y muestra tu IP pública.

---

## 🔧 Características

| ✅ | Funcionalidad |
|---|---------------|
| ✔️ | Banner ASCII atractivo con `pyfiglet` |
| ✔️ | Menú interactivo con `InquirerPy` |
| ✔ | Validación y análisis completo de números móviles (`phonenumbers`) |
| ✔️ | Rastrear IP con geolocalización (`ipwho.is`) |
| ✔️ | Mostrar IP pública del equipo (`ipify`) |
| ✔️ | Salida en tablas bien formateadas (`tabulate`) |
| ✔ | Soporte completo en Español |

---

## ⚙ Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu_usuario/tracker.git
cd tracker

# (Opcional) Crear entorno virtual
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

> **Nota**: Las versiones mínimas exigidas están en `pyproject.toml`.  
> • `python >= 3.14`  
> • `inquirerpy >= 0.3.4`  
> • `phonenumbers >= 9.0.33`  
> • `pyfiglet >= 1.0.4`  
> • `python-dotenv >= 1.2.2`  
> • `tabulate >= 0.10.0`

Para ejecutar la aplicación, simplemente:

```bash
python main.py
```

---

## 🚀 Uso rápido

1. Se abre el banner **Tracker**.  
2. Selecciona una opción:
   * **Numero de celular** → escribe el número (ej. `+5491155551234`) y presiona Enter.  
   * **Rastrear ip** → ingresa una IP y obtén su ubicación.  
   * **Cual es mi ip** → muestra tu IP pública.  
3. Para salir, elige **Salir**.

---

## 🤝 Cómo contribuir

1. Haz un fork del proyecto.  
2. Crea una rama para tu feature: `git checkout -b feature/nueva_funcionalidad`.  
3. Realiza commits claros y descriptivos.  
4. Empuja tu rama: `git push origin feature/nueva_funcionalidad`.  
5. Envía un Pull Request a la rama `main` y espera la revisión.

**Requisitos de contribución**

- Mantener la coherencia de tipo de archivo (`.py`).  
- Los nuevos módulos deben seguir el mismo patrón de interacción y tablas.  
- Proporcionar pruebas unitarias (recomendado, aunque opcional).  

--- 

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

--- 

¡Gracias por usar **Tracker**! 🎉
