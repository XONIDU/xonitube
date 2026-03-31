# 🎬 XONITUBE by Darian Alberto Camacho Salas

Reproductor de YouTube desde terminal para PC de gama baja (1GB RAM)

## ⚠️ ADVERTENCIA
Este código tiene **únicamente fines educativos y de uso personal**. No debe utilizarse para infringir los términos de servicio de YouTube.

## 📁 Estructura del Proyecto

```
xonitube/
├── start.py                 # 🟢 LANZADOR UNIVERSAL (¡SOLO EJECUTA ESTE!)
├── xonitube.py              # 🔵 PROGRAMA PRINCIPAL (buscador/reproductor)
├── requisitos.txt           # Dependencias del proyecto
└── README.md                # Este archivo
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

El instalador automático te guiará para instalar mpv y yt-dlp si es necesario.

## 🐧 **PARA LINUX**

```bash
# Abre terminal y escribe:
python3 start.py
```

En distribuciones como Ubuntu/Debian/Arch, **start.py instalará mpv y yt-dlp automáticamente** (solicitará contraseña sudo).

## 🍎 **PARA macOS**

```bash
# Abre terminal y escribe:
python3 start.py
```

Si tienes Homebrew, **start.py instalará mpv y yt-dlp automáticamente**.

## 📦 **¿QUÉ HACE start.py POR DENTRO?**

Cuando ejecutas `start.py`, automáticamente:

1. 🔍 **Detecta** si estás en Windows, Linux o Mac
2. 📋 **Verifica** si tienes instalado Python, mpv y yt-dlp
3. 📥 **Instala automáticamente** las dependencias que faltan:
   - **Linux:** Ejecuta `sudo apt install mpv yt-dlp` (o `pacman -S` en Arch)
   - **Mac:** Ejecuta `brew install mpv` y `pip install yt-dlp`
   - **Windows:** Muestra instrucciones y ofrece instalación automática de yt-dlp
4. 🚀 **Ejecuta** `xonitube.py` (el programa principal)

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

### ❌ **"Python no está instalado"**
```bash
# Descarga Python desde:
https://www.python.org/downloads/
```

### ❌ **"No se encontró el comando mpv" en Linux**
```bash
# start.py ya lo instala automáticamente, pero si falla:
# Debian/Ubuntu
sudo apt install mpv

# Arch
sudo pacman -S mpv
```

### ❌ **"No se encontró el comando yt-dlp" en Linux**
```bash
# start.py ya lo instala automáticamente, pero si falla:
# Debian/Ubuntu
sudo apt install yt-dlp

# Arch
sudo pacman -S yt-dlp
```

### ❌ **"Se escucha audio pero no se ve video"**
```bash
# start.py ya configura el backend x11 automáticamente
# Si persiste, verificar backends disponibles:
mpv --vo=help
```

### ❌ **"La ventana se maximiza y da lag"**
El programa ya fuerza un tamaño fijo de **640x360** para evitar lag. Si aún así maximizas, tendrás descincronización. Usa la opción de descarga para ver el video sin lag.

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

- 📸 **Instagram:** [@xonidu](https://instagram.com/xonidu)
- 📧 **Email:** xonidu@gmail.com
- 💻 **GitHub:** [XONIDU/xonitube](https://github.com/XONIDU/xonitube)

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

