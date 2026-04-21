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
git clone https://github.com/XONIDU/xonitube.git
cd xonitube
python3 start.py
```

### 📥 Opción 3: Instalación manual
```bash
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

### 5️⃣ Elegir acción (OPTIMIZADO PARA 1GB RAM)
```
OPCIONES OPTIMIZADAS:
  1. Streaming (sin descarga - mas CPU/red)
  2. Descargar + Reproducir (guarda permanentemente)
  3. Solo descargar (guarda permanentemente)
  4. Descargar + Reproducir + BORRAR (OPTIMO para 1GB RAM)

💡 RECOMENDADO: Opcion 4 (descarga, reproduce y borra)
   - Menos lag que streaming
   - No ocupa espacio en disco
   - Ideal para 1GB RAM
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
Linux:   /home/tu_usuario/Videos/XoniTube/
Windows: C:\Users\TuUsuario\Videos\XoniTube\
Mac:     /Users/tu_usuario/Videos/XoniTube/
```

Los archivos temporales (Opción 4) se guardan en `/tmp/xonitube_temp/` y se borran automáticamente.

## 📊 **COMPARATIVA DE OPCIONES**

| Opción | Comportamiento | RAM | Disco | Lag | Recomendado |
|--------|---------------|-----|-------|-----|-------------|
| 1 | Streaming directo | Alta | No | Sí | ❌ |
| 2 | Descargar + Guardar | Media | Permanente | No | ⚠️ |
| 3 | Solo descargar | Baja | Permanente | - | ⚠️ |
| 4 | Descargar + Borrar | **Baja** | **Temporal** | **No** | ✅ |

## 🔧 **PROBLEMAS COMUNES (Y SOLUCIONES)**

### ❌ "Failed to recognize file format"
El error está corregido en v6.5.0. Actualiza:
```bash
yay -S xonitube --rebuild
```

### ❌ "Python no está instalado"
```bash
# Descarga Python desde:
https://www.python.org/downloads/
```

### ❌ "No se encontró el comando mpv" en Linux
```bash
# Debian/Ubuntu
sudo apt install mpv

# Arch
sudo pacman -S mpv
```

### ❌ "No se encontró el comando yt-dlp" en Linux
```bash
# Debian/Ubuntu
sudo apt install yt-dlp

# Arch
sudo pacman -S yt-dlp
```

### ❌ "Se escucha audio pero no se ve video"
```bash
# Verificar backends disponibles:
mpv --vo=help

# Instalar controladores si es necesario:
sudo pacman -S xf86-video-intel  # Intel
sudo pacman -S xf86-video-nouveau # NVIDIA
```

### ❌ "La ventana se maximiza y da lag"
El programa fuerza tamaño fijo 640x360. Usa la **Opción 4** (descarga + borra) para eliminar el lag.

## ⚡ **OPTIMIZADO PARA 1GB RAM**

| Configuración | Valor | Beneficio |
|---------------|-------|-----------|
| Tamaño ventana | 640x360 | No satura el procesador |
| Método por defecto | Opción 4 | Descarga, reproduce y borra |
| Archivos temporales | /tmp | Se borran automáticamente |
| Cache | 30 segundos | Equilibrio RAM/fluidez |
| Sin subtítulos | Sí | Ahorra CPU |

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
- ✅ **Opción 4 por defecto**: descarga, reproduce y borra
- ✅ **Ventana de tamaño fijo** para evitar lag
- ✅ Soporta **9 calidades diferentes** (desde peor hasta solo audio)
- ✅ Archivos temporales en `/tmp/xonitube_temp/` (se borran solos)

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
║   • Opción 4: descarga, reproduce y borra               ║
║   • Instalación automática                              ║
║   • Ventana fija sin lag                                ║
╚══════════════════════════════════════════════════════════╝
```

**XONIDU** - Enseñando automatización, construyendo conocimiento

