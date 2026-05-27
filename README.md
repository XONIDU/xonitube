# 🎬 XONITUBE by Darian Alberto Camacho Salas

Reproductor de YouTube desde terminal para PC de gama baja (1GB RAM)

## ⚠️ ADVERTENCIA

Este código tiene **únicamente fines educativos y de uso personal**. Los videos descargados deben ser para uso privado, no deben redistribuirse ni usarse comercialmente.

## 📁 Estructura del Proyecto

```
xonitube/
├── start.py                 # 🟢 LANZADOR UNIVERSAL
├── xonitube.py              # 🔵 PROGRAMA PRINCIPAL
├── requisitos.txt         # Dependencias
└── README.md                # Este archivo
```

## 🚀 **INSTALACIÓN**

### Arch Linux (AUR)
```bash
yay -S xonitube
xonitube
```

### Otras distribuciones / Windows / Mac
```bash
git clone https://github.com/XONIDU/xonitube.git
cd xonitube
python3 start.py
```

### Opción 2 – Comando `xoninstall` (recomendado para futuras herramientas XONI)

Agrega la siguiente función a tu `~/.bashrc` con un solo comando:

```bash
echo 'xoninstall() { if [ -z "$1" ]; then echo "Uso: xoninstall <repo>"; echo "Ej: xoninstall xoniran"; else git clone "https://github>
```

Luego simplemente escribe:

```bash
xoninstall xonitube
cd xonitube
pip install -r requisitos.txt
python start.py
```

> **Nota:** Esta función te servirá para instalar cualquier otra herramienta futura de XONIDU (por ejemplo `xoninstall xonicli`).



## 🎯 **CÓMO USAR XONITUBE**

### 1️⃣ Buscar videos
```
Buscar → kendrick lamar
```

### 2️⃣ Elegir cuántos resultados
```
Cuantos resultados? (1-15, Enter=5): 5
```

### 3️⃣ Seleccionar video
```
Numero de video (Enter para nueva busqueda): 1
```

### 4️⃣ Elegir calidad
```
CALIDADES:
  1. Peor calidad (mas rapido)
  2. 144p | 3. 240p | 4. 360p | 5. 480p
  6. 720p | 7. 1080p | 8. Mejor calidad | 9. Solo audio
```

### 5️⃣ Elegir acción (OPTIMIZADO PARA 1GB RAM)
```
OPCIONES:
  1. Streaming (sin descarga)
  2. Descargar + Reproducir (guarda)
  3. Solo descargar
  4. Descargar + Reproducir + BORRAR (RECOMENDADO)

💡 Opción 4: descarga, reproduce y borra - Menos lag, no ocupa espacio
```

### 6️⃣ Controles durante reproducción
- **← →** : Retroceder/Avanzar 5s
- **Space** : Pausa
- **↑ ↓** : Volumen
- **q** : Salir
- **Ctrl+C** : Volver al menú

## 💾 **UBICACIÓN DE DESCARGAS**

| Tipo | Ruta |
|------|------|
| Permamentes | `~/Videos/XoniTube/` |
| Temporales (Opción 4) | `/tmp/xonitube_temp/` (se borran solos) |

## 📊 **COMPARATIVA DE OPCIONES**

| Opción | RAM | Disco | Lag | Recomendado |
|--------|-----|-------|-----|-------------|
| 1 (Streaming) | Alta | No | Sí | ❌ |
| 2 (Guardar) | Media | Permanente | No | ⚠️ |
| 3 (Solo guardar) | Baja | Permanente | - | ⚠️ |
| 4 (Descargar + Borrar) | **Baja** | **Temporal** | **No** | ✅ |

## 🔧 **PROBLEMAS COMUNES**

### ❌ "Failed to recognize file format"
```bash
yay -S xonitube --rebuild
```

### ❌ "No se encontró mpv o yt-dlp"
```bash
# Arch
sudo pacman -S mpv yt-dlp

# Debian/Ubuntu
sudo apt install mpv yt-dlp
```

### ❌ "Se escucha audio pero no se ve video"
```bash
mpv --vo=help
sudo pacman -S xf86-video-intel  # Intel
```

### ❌ "Lag al maximizar ventana"
Usa la **Opción 4** (descarga + borra). El programa ya fuerza tamaño 640x360.

## ⚡ **OPTIMIZADO PARA 1GB RAM**

| Configuración | Valor |
|---------------|-------|
| Tamaño ventana | 640x360 |
| Método por defecto | Opción 4 |
| Archivos temporales | `/tmp` (se borran) |
| Sin subtítulos | Sí |

## 📞 **CONTACTO**

- **Instagram:** @xonidu
- **Email:** xonidu@gmail.com
- **GitHub:** XONIDU/xonitube
- **AUR:** xonitube

## 🔄 **ACTUALIZAR**

```bash
# Desde AUR
yay -S xonitube --rebuild

# Desde GitHub
cd xonitube && git pull && python3 start.py
```

## 🎉 **¡LISTO!**

```
╔══════════════════════════════════════════════════════════╗
║   XONITUBE 2026 - Optimizado para 1GB RAM                ║
║   por Darian Alberto Camacho Salas                       ║
║                                                          ║
║   • Streaming o descarga                                ║
║   • Opción 4: descarga, reproduce y borra               ║
║   • Instalación automática                              ║
║   • Sin lag, sin ocupar espacio                         ║
╚══════════════════════════════════════════════════════════╝
```

**XONIDU** - Enseñando automatización, construyendo conocimiento

