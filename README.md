# 🎬 XONITUBE by Darian Alberto Camacho Salas

Reproductor de videos en línea para PC de gama baja (Asus Eee PC con 1GB RAM)

---

## ⚙️ ¿Qué hace?

- 🔍 **Búsqueda rápida** desde terminal
- 📋 **Resultados numerados** para fácil selección
- 🎮 **Controles de reproducción**: ← → (retroceder/avanzar), Space (pausa), ↑ ↓ (volumen)
- 🛡️ **Método anti-bloqueo** por defecto (evita error 403)
- 📊 **7 opciones de calidad**: Peor, 144p, 240p, 360p, 480p, Mejor, Solo audio
- ⚡ **Optimizado** para 1GB RAM y procesador Celeron
- 🖥️ **Interfaz conversacional** sin entorno gráfico
- 🧹 **Autolimpieza**: No guarda archivos temporales
- 🎯 **Video forzado**: Usa múltiples backends para garantizar que el video se vea

---

## 🚀 Requisitos de Instalación

```bash
# Somos XONINDU
# Creador: Darian Alberto Camacho Salas

# XoniTube v5.1 - Buscador de YouTube para terminal
# Metodo anti-bloqueo por defecto con video forzado

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

---

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
   Cuantos resultados? (1-15, Enter=5): 5
   ```

4. **Selecciona un video de la lista:**
   ```
   Numero de video (Enter para nueva busqueda): 1
   ```

5. **Elige la calidad:**
   ```
   CALIDADES DISPONIBLES:
     1. Peor calidad (mas rapida, ahorro de datos)
     2. 144p (muy baja)
     3. 240p (baja)
     4. 360p (media)
     5. 480p (estandar)
     6. 720p (HD)
     7. 1080p (Full HD)
     8. Mejor calidad disponible (mas lenta)
     9. Solo audio (sin video)
   
   Elige una opcion (1-9, Enter=1): 1
   ```

6. **Controla la reproducción:**
   - ← → : Retroceder / Avanzar 5 segundos
   - ↑ ↓ : Subir / Bajar volumen
   - Space : Pausa/Reanudar
   - q : Salir de la reproducción
   - Ctrl+C : Volver al menú

7. **Repite o busca otro video**

---

## 🛠️ Solución de problemas de video

Si el audio se escucha pero **no se ve el video**, XoniTube probará automáticamente diferentes backends de video (x11, sdl, vaapi, vdpau, drm, xv) hasta encontrar uno que funcione.

### 🔍 Diagnóstico manual

Si el problema persiste, ejecuta estos comandos para verificar los backends soportados por tu sistema:

```bash
# Listar backends de video disponibles
mpv --vo=help

# Listar backends de audio disponibles
mpv --ao=help
```

Asegúrate de que **x11** aparezca en la lista de backends de video. Si no aparece, instala los controladores apropiados para tu GPU:

```bash
# Para Intel
sudo apt install xserver-xorg-video-intel

# Para NVIDIA (controlador libre nouveau)
sudo apt install xserver-xorg-video-nouveau

# Para AMD/ATI
sudo apt install xserver-xorg-video-ati

# Controlador VESA genérico (si no sabes cuál es tu GPU)
sudo apt install xserver-xorg-video-vesa
```

Después de instalar los controladores, reinicia X (cerrando sesión y volviendo a entrar) o reinicia el sistema.

---

## 💡 Características Técnicas

- **Lenguaje**: Python 3
- **Dependencias mínimas**: Solo requiere yt-dlp y mpv
- **Optimizado para**: Asus Eee PC con 1GB de RAM y procesador Celeron
- **Método de reproducción**: Pipe entre yt-dlp y mpv para evitar bloqueos (no guarda archivos)
- **Backends de video**: Prueba automática de x11, sdl, vaapi, vdpau, drm, xv
- **Cache**: Configurado para reproducción fluida en conexiones lentas
- **Autolimpieza**: Elimina cualquier archivo temporal al terminar

---

## ❓ ¿Dudas o sugerencias?

Si tienes preguntas sobre los conceptos de programación, automatización o mejoras para este proyecto:

- 📸 **Instagram**: @xonidu
- 📘 **Facebook**: xonidu
- 📧 **Email**: xonidu@gmail.com

