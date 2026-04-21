# 🎬 XONITUBE by Darian Alberto Camacho Salas

Reproductor de YouTube desde terminal para PC de gama baja (1GB RAM)

## ⚠️ ADVERTENCIA
Este código tiene **únicamente fines educativos y de uso personal**. No debe utilizarse para infringir los términos de servicio de YouTube.

## 📁 Estructura del Proyecto

```
xonitube/
├── start.py                 # 🟢 LANZADOR UNIVERSAL (¡SOLO EJECUTA ESTE!)
├── xonitube.py              # 🔵 PROGRAMA PRINCIPAL (buscador/reproductor)
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Este archivo
```

## 🚀 **MÉTODOS DE INSTALACIÓN**

### 📦 Opción 1: Instalación desde AUR (Arch Linux)
```bash
yay -S xonitube
xonitube
```

### 🐙 Opción 2: Instalación desde GitHub
```bash
# Clonar el repositorio
git clone https://github.com/XONIDU/xonitube.git
cd xonitube

# Ejecutar el lanzador
python3 start.py
```

### 📥 Opción 3: Instalación manual
```bash
# Descargar el ZIP desde GitHub
wget https://github.com/XONIDU/xonitube/archive/refs/heads/main.zip
unzip main.zip
cd xonitube-main
python3 start.py
```

## 🚀 **ASÍ DE FÁCIL: SOLO EJECUTA start.py**

**¡Ya no necesitas hacer nada más!** El archivo `start.py` hace TODO por ti:

✅ Detecta automáticamente tu sistema operativo  
✅ Verifica qué dependencias faltan (mpv, yt-dlp, python)  
✅ **Las instala automáticamente** con los comandos correctos  
✅ Ejecuta el programa principal  

## 🪟 **PARA WINDOWS**

```bash
# Abre CMD o PowerShell y escribe:
python start.py
```

## 🐧 **PARA LINUX**

```bash
# Abre terminal y escribe:
python3 start.py
```

## 🍎 **PARA macOS**

```bash
# Abre terminal y escribe:
python3 start.py
```

## 🎯 **CÓMO USAR XONITUBE**

### 1️⃣ Buscar videos
```
Buscar → kendrick lamar
```

### 2️⃣ Elegir cuántos resultados
```
Cuantos resultados? (1-15, Enter=5): 5
```

### 3️⃣ Seleccionar video por número
```
Numero de video (Enter para nueva busqueda): 1
```

### 4️⃣ Elegir calidad
```
CALIDADES DISPONIBLES:
  1. Peor calidad (mas rapido, ahorro de datos)
  2. 144p (muy baja)
  3. 240p (baja)
  4. 360p (media)
  5. 480p (estandar)
  6. 720p (HD)
  7. 1080p (Full HD)
  8. Mejor calidad disponible (mas lento)
  9. Solo audio (sin video)
```

### 5️⃣ Elegir acción
```
OPCIONES:
  1. Reproducir ahora (streaming)
  2. Guardar y luego reproducir
  3. Solo guardar (no reproducir)
```

### 6️⃣ Controlar reproducción
- **← →** : Retroceder/Avanzar 5 segundos
- **Space** : Pausa/Reanudar
- **↑ ↓** : Subir/Bajar volumen
- **q** : Salir de la reproducción
- **Ctrl+C** : Volver al menú

## 💾 **DESCARGAS**

Los videos que decidas guardar se almacenan automáticamente en:

```
Windows: C:\Users\TuUsuario\Videos\XoniTube\
Linux:   /home/tu_usuario/Videos/XoniTube/
Mac:     /Users/tu_usuario/Videos/XoniTube/
```

## 🔧 **PROBLEMAS COMUNES (Y SOLUCIONES)**

### ❌ **"Error parsing commandline option geometry"**
El error ya está corregido en la versión v6.4.1. Actualiza:
```bash
# Desde AUR
yay -S xonitube --rebuild

# Desde GitHub
cd xonitube
git pull
python3 start.py
```

### ❌ **"Python no está instalado"**
```bash
# Descarga Python desde:
https://www.python.org/downloads/
```

### ❌ **"No se encontró el comando mpv" en Linux**
```bash
# Debian/Ubuntu
sudo apt install mpv

# Arch
sudo pacman -S mpv
```

### ❌ **"No se encontró el comando yt-dlp" en Linux**
```bash
# Debian/Ubuntu
sudo apt install yt-dlp

# Arch
sudo pacman -S yt-dlp
```

### ❌ **"Se escucha audio pero no se ve video"**
```bash
# Verificar backends disponibles:
mpv --vo=help

# Instalar controladores si es necesario:
sudo pacman -S xf86-video-intel  # Intel
sudo pacman -S xf86-video-nouveau # NVIDIA
```

### ❌ **"La ventana se maximiza y da lag"**
El programa ya fuerza un tamaño fijo de **640x360** para evitar lag. Usa la opción de descarga (opción 2 o 3) para ver el video sin lag.

## ⚡ **OPTIMIZADO PARA 1GB RAM**

| Configuración | Valor | Beneficio |
|---------------|-------|-----------|
| Tamaño ventana | 640x360 | No satura el procesador |
| Cache | 30 segundos | Equilibrio RAM/fluidez |
| Backend video | x11 | Máxima compatibilidad |
| Sin subtítulos | Sí | Ahorra CPU |
| Perfil rápido | Sí | Decodificación eficiente |
| Descarga local | Opcional | Ver sin lag después de descargar |

## 📞 **¿NECESITAS AYUDA?**

- 📸 **Instagram:** @xonidu
- 📧 **Email:** xonidu@gmail.com
- 💻 **GitHub:** XONIDU/xonitube
- 📦 **AUR:** xonitube

## ✅ **LO QUE PUEDES HACER (Y LO QUE NO)**

| ✅ SÍ | ❌ NO |
|-------|-------|
| Ver videos de YouTube | Descargar contenido con copyright |
| Guardar videos para ver offline | Usarlo comercialmente |
| Aprender automatización | Quitar los créditos |
| Probar en tu Eee PC | Infringir términos de servicio |

## 📋 **NOTAS IMPORTANTES**

- ✅ Funciona en **Windows, Linux y Mac** con Python 3.6+
- ✅ **Instalación automática** de dependencias vía `start.py`
- ✅ Optimizado para **1GB RAM** y procesadores antiguos
- ✅ **Opción de guardar video** antes de reproducir
- ✅ **Ventana de tamaño fijo** para evitar lag
- ✅ Soporta **9 calidades diferentes** (desde peor hasta solo audio)
- ✅ Los videos guardados se almacenan en **~/Videos/XoniTube/**

## 🔄 **ACTUALIZAR XONITUBE**

```bash
# Desde AUR
yay -S xonitube --rebuild

# Desde GitHub
cd xonitube
git pull
python3 start.py
```

## 🎉 **¡LISTO!**

```
╔══════════════════════════════════════════════════════════╗
║   XONITUBE 2026 - Hecho con ❤️                           ║
║   por Darian Alberto Camacho Salas                       ║
║                                                          ║
║   Características:                                       ║
║   • Streaming directo o descarga                        ║
║   • Optimizado para 1GB RAM                             ║
║   • Instalación automática                              ║
║   • Ventana fija sin lag                                ║
╚══════════════════════════════════════════════════════════╝
```

**XONIDU** - Enseñando automatización, construyendo conocimiento

