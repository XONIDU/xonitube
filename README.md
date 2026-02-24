# 🎬 XONITUBE by Darian Alberto Camacho Salas

**Advertencia:** Este código tiene únicamente fines educativos y de uso personal. Está diseñado para enseñar principios de automatización de búsquedas y reproducción de contenido multimedia desde la terminal. No debe utilizarse para infringir los términos de servicio de YouTube o para uso comercial sin las autorizaciones correspondientes.

## 🎯 Objetivo

Este proyecto tiene como propósito enseñar cómo automatizar la búsqueda y reproducción de videos de YouTube desde la terminal, optimizado para equipos con recursos limitados como el Asus Eee PC con 1GB de RAM. Está diseñado como una herramienta educativa para practicar conceptos de web scraping, interfaz de terminal y reproducción multimedia.

## ⚙️ ¿Qué hace?

- **🔍 Búsqueda Rápida**: Busca videos en YouTube directamente desde la terminal sin necesidad de abrir un navegador.
- **📋 Lista de Resultados**: Muestra los resultados numerados para fácil selección.
- **🎮 Controles de Reproducción**: Permite pausar, avanzar, retroceder y controlar volumen durante la reproducción.
- **⚡ Optimizado para Recursos Limitados**: Funciona perfectamente en equipos con 1GB de RAM como el Asus Eee PC.
- **🛡️ Método Anti-Bloqueo**: Incluye un sistema que evita los errores 403 de YouTube (opción 8, ahora por defecto).
- **📊 Selección de Calidad**: Elige entre 7 opciones de calidad, desde la más baja hasta solo audio.
- **⏯️ Retroceso y Avance**: Durante la reproducción puedes retroceder o avanzar usando las flechas ← →.
- **🖥️ Interfaz de Terminal**: Interfaz limpia y conversacional que no requiere entorno gráfico.

## 🚀 Requisitos de Instalación

```bash
# Somos XONINDU
# Creador: Darian Alberto Camacho Salas

# XoniTube v4.2.0 - Buscador de YouTube para terminal
# Metodo anti-bloqueo por defecto

# Arch Linux
sudo pacman -S python python-pip mpv yt-dlp
# No se necesitan paquetes adicionales de pip

# Ubuntu y derivados (Debian, Linux Mint, etc.)
sudo apt update
sudo apt install python3 python3-pip mpv yt-dlp -y
# No se necesitan paquetes adicionales de pip

# Windows
# Instalar Python desde: https://www.python.org/downloads/
pip install yt-dlp
# Instalar mpv desde: https://mpv.io/installation/
# Nota: En Windows, el metodo anti-bloqueo puede requerir configuracion adicional

# Verificar instalacion
yt-dlp --version
mpv --version

# Ejecucion:
python xonitube.py
```

## 📖 Cómo Usarlo

1. **Ejecuta el programa:**
   ```bash
   python xonitube.py
   ```

2. **Escribe tu búsqueda:**
   ```
   Buscar? → kendrick lamar
   ```

3. **Elige cuántos resultados ver:**
   ```
   Cuantos resultados? (1-10, Enter=5): 5
   ```

4. **Selecciona un video de la lista:**
   ```
   Que video? (1-5, Enter=menu): 1
   ```

5. **Elige la calidad:**
   ```
   CALIDADES DISPONIBLES:
     1. Peor calidad (mas rapido)
     2. 144p
     3. 240p
     4. 360p
     5. 480p
     6. Mejor calidad (mas lento)
     7. Solo audio
   
   Elige calidad (1-7, Enter=1): 3
   ```

6. **Controla la reproducción:**
   - **← →** : Retroceder / Avanzar 5 segundos
   - **↑ ↓** : Subir / Bajar volumen
   - **Space** : Pausa/Reanudar
   - **q** : Salir de la reproducción
   - **Ctrl+C** : Volver al menú

7. **Repite o busca otro video**

## 💡 Características Técnicas

- **Lenguaje**: Python 3
- **Dependencias mínimas**: Solo requiere yt-dlp y mpv
- **Optimizado para**: Asus Eee PC con 1GB de RAM y procesador Celeron
- **Método de reproducción**: Pipe entre yt-dlp y mpv para evitar bloqueos
- **Cache**: Configurado para reproducción fluida en conexiones lentas

## ❓ ¿Dudas o sugerencias?

Si tienes preguntas sobre los conceptos de programación, automatización o mejoras para este proyecto:

- **📸 Instagram**: @xonidu
- **📘 Facebook**: xonidu
- **📧 Email**: xonidu@gmail.com

**Nota:** Este proyecto es únicamente para fines educativos y de aprendizaje de automatización. No está diseñado para descargar contenido con derechos de autor sin permiso ni para uso comercial. Respeta siempre los términos de servicio de las plataformas.
```
