# 🎬 XONITUBE v4.2.0

##  Darian Alberto Camacho Salas

Reproductor de videos en línea para PC de gama baja

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

---

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
python start.py
```

---

## 📖 Cómo Usarlo

1. **Ejecuta el programa:**
   ```bash
   python start.py
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
   - ← → : Retroceder / Avanzar 5 segundos
   - ↑ ↓ : Subir / Bajar volumen
   - Space : Pausa/Reanudar
   - q : Salir de la reproducción
   - Ctrl+C : Volver al menú

7. **Repite o busca otro video**

---

## 💡 Características Técnicas

- **Lenguaje**: Python 3
- **Dependencias mínimas**: Solo requiere yt-dlp y mpv
- **Optimizado para**: Asus Eee PC con 1GB de RAM y procesador Celeron
- **Método de reproducción**: Pipe entre yt-dlp y mpv para evitar bloqueos (no guarda archivos)
- **Cache**: Configurado para reproducción fluida en conexiones lentas
- **Autolimpieza**: Elimina cualquier archivo temporal al terminar

---

## ❓ ¿Dudas o sugerencias?

Si tienes preguntas sobre los conceptos de programación, automatización o mejoras para este proyecto:

- 📸 **Instagram**: @xonidu
- 📘 **Facebook**: xonidu
- 📧 **Email**: xonidu@gmail.com

## SOMOS XONIDU
