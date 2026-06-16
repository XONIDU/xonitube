# 🎬 XONITUBE by Darian Alberto Camacho Salas

Reproductor de YouTube desde terminal para PC de gama baja (1GB RAM)

## ⚠️ ADVERTENCIA

Este código tiene **únicamente fines educativos y de uso personal**. Los videos descargados deben ser para uso privado, no deben redistribuirse ni usarse comercialmente.

## 📁 Estructura del Proyecto

```
xonitube/
├── start.py                 # 🟢 LANZADOR UNIVERSAL (¡SOLO EJECUTA ESTE!)
├── xonitube.py              # 🔵 PROGRAMA PRINCIPAL (buscador/reproductor)
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Este archivo
```

## 🚀 **MÉTODOS DE INSTALACIÓN**

### 🐧 Linux (cualquier distribución)

#### 📦 Opción 1: Desde AUR (Arch Linux / EndeavourOS / Manjaro)
```bash
yay -S xonitube
xonitube
```

#### 🐙 Opción 2: Usando el instalador universal (Recomendado)
```bash
git clone https://github.com/XONIDU/xonitube.git
cd xonitube
python3 start.py
```

El instalador detecta automáticamente tu distribución e instala `mpv` y `yt-dlp` con el gestor de paquetes correcto (apt, pacman, dnf, zypper, etc.).

#### 📥 Opción 3: Instalación manual
```bash
# Instalar dependencias
# Debian/Ubuntu/Mint
sudo apt install mpv yt-dlp

# Arch/Manjaro
sudo pacman -S mpv yt-dlp

# Fedora
sudo dnf install mpv yt-dlp

# openSUSE
sudo zypper install mpv yt-dlp

# Clonar y ejecutar
git clone https://github.com/XONIDU/xonitube.git
cd xonitube
python3 xonitube.py
```

---

### 🪟 Windows

#### ⚡ Instalación automática (recomendada)
```cmd
# Abre PowerShell o CMD como administrador
git clone https://github.com/XONIDU/xonitube.git
cd xonitube
python start.py
```

El instalador verificará e instalará automáticamente `yt-dlp` (mediante pip) y te guiará para instalar `mpv` manualmente si es necesario.

#### 📥 Instalación manual paso a paso

1. **Instalar Python 3.6+**  
   Descarga desde [python.org](https://www.python.org/downloads/) y marca "Add Python to PATH"

2. **Instalar mpv**  
   - Descarga el archivo `.7z` desde [mpv.io/installation](https://mpv.io/installation/)  
   - Extrae a `C:\mpv`  
   - Agrega `C:\mpv` a las variables de entorno del sistema (PATH)

3. **Instalar yt-dlp**  
   ```cmd
   pip install yt-dlp
   ```

4. **Ejecutar XONITUBE**  
   ```cmd
   git clone https://github.com/XONIDU/xonitube.git
   cd xonitube
   python xonitube.py
   ```


### Opción 3 – Comando `xoninstall` (recomendado para futuras herramientas XONI)

Agrega la siguiente función a tu `~/.bashrc` con un solo comando:

```bash
echo 'xoninstall() { if [ -z "$1" ]; then echo "Uso: xoninstall <repo>"; echo "Ej: xoninstall xoniran"; else git clone "https>
```

Luego simplemente escribe:

```bash
xoninstall xonitube
cd xonitube
pip install -r requisitos.txt
python start.py
```

---

### 🍎 macOS

#### ⚡ Instalación automática (recomendada)
```bash
git clone https://github.com/XONIDU/xonitube.git
cd xonitube
python3 start.py
```

El instalador usará Homebrew para instalar `mpv` y `yt-dlp` si es posible, o recurrirá a pip.

#### 📥 Instalación manual con Homebrew
```bash
# Instalar dependencias
brew install mpv yt-dlp

# Clonar y ejecutar
git clone https://github.com/XONIDU/xonitube.git
cd xonitube
python3 xonitube.py
```

---

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

### 5️⃣ Elegir acción **(OPTIMIZADO PARA 1GB RAM)**

Por defecto se selecciona la **Opción 4** (solo presiona Enter):

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

| Tipo | Ruta |
|------|------|
| Permanentes | `~/Videos/XoniTube/` (Linux/macOS) o `%USERPROFILE%\Videos\XoniTube\` (Windows) |
| Temporales (Opción 4) | `/tmp/xonitube_temp/` (Linux/macOS) o `%TEMP%\xonitube_temp\` (Windows) |

## 📊 **COMPARATIVA DE OPCIONES**

| Opción | Comportamiento | RAM | Disco | Lag | Recomendado |
|--------|---------------|-----|-------|-----|-------------|
| 1 | Streaming directo | Alta | No | Sí | ❌ |
| 2 | Descargar + Guardar | Media | Permanente | No | ⚠️ |
| 3 | Solo descargar | Baja | Permanente | - | ⚠️ |
| 4 | Descargar + Borrar | **Baja** | **Temporal** | **No** | ✅ |

## 🔧 **PROBLEMAS COMUNES (Y SOLUCIONES)**

### ❌ "Failed to recognize file format"
El error está corregido en v6.5.0+. Actualiza:
```bash
# Desde AUR
yay -S xonitube --rebuild

# Desde GitHub
cd xonitube && git pull && python3 start.py
```

### ❌ "Python no está instalado"
Descarga Python desde [python.org](https://www.python.org/downloads/)

### ❌ "No se encontró el comando mpv"

#### Linux
```bash
# Debian/Ubuntu/Mint
sudo apt install mpv

# Arch/Manjaro
sudo pacman -S mpv

# Fedora
sudo dnf install mpv

# openSUSE
sudo zypper install mpv
```

#### Windows
Descarga y extrae mpv en `C:\mpv` y agrégalo al PATH.

#### macOS
```bash
brew install mpv
```

### ❌ "No se encontró el comando yt-dlp"

#### Linux
```bash
# Debian/Ubuntu
sudo apt install yt-dlp

# Arch
sudo pacman -S yt-dlp

# Fedora
sudo dnf install yt-dlp

# O con pip (cualquier SO)
pip install yt-dlp
```

#### Windows
```cmd
pip install yt-dlp
```

#### macOS
```bash
brew install yt-dlp
```

### ❌ "Se escucha audio pero no se ve video"
```bash
# Verificar backends disponibles:
mpv --vo=help

# Instalar controladores si es necesario (Linux):
# Intel
sudo pacman -S xf86-video-intel
# NVIDIA
sudo pacman -S xf86-video-nouveau
```

### ❌ "Lag al maximizar ventana"
El programa fuerza tamaño fijo 640x360. Usa la **Opción 4** (descarga + borra) para eliminar el lag.

## ⚡ **OPTIMIZADO PARA 1GB RAM**

| Configuración | Valor | Beneficio |
|---------------|-------|-----------|
| Tamaño ventana | 640x360 | No satura el procesador |
| Método por defecto | Opción 4 | Descarga, reproduce y borra |
| Archivos temporales | `/tmp` o `%TEMP%` | Se borran automáticamente |
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
| Ver videos de YouTube | Descargar contenido con copyright para redistribuir |
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
- ✅ Archivos temporales se eliminan automáticamente

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

