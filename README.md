#XONITUBE by Darian Alberto Camacho Salas

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

---

## 🚀 Requisitos

```bash
# Somos XONINDU
# Creador: Darian Alberto Camacho Salas

# Arch Linux
sudo pacman -S python python-pip mpv yt-dlp

# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip mpv yt-dlp -y

# Windows
# Python: https://www.python.org/downloads/
pip install yt-dlp
# MPV: https://mpv.io/installation/

# Verificar
yt-dlp --version
mpv --version

## 📥 Instalación

Clona el repositorio desde GitHub:

```bash
git clone https://github.com/XONIDU/xonitube.git
cd xonitube
```

# Ejecutar
python start.py

#o

python3 start.py
```

---

## 📖 Uso básico

```
Buscar? → kendrick lamar
Cuantos resultados? (1-10, Enter=5): 5
Que video? (1-5, Enter=menu): 1
Elige calidad (1-7, Enter=1): 3
```

**Controles durante reproducción:**
- ← → : Retroceder/Avanzar 5s
- Space : Pausa
- ↑ ↓ : Volumen
- q : Salir
- Ctrl+C : Volver al menú

---

## 💡 Características técnicas

- **Lenguaje**: Python 3
- **Dependencias**: yt-dlp + mpv
- **Método**: Pipe streaming (sin archivos)
- **Cache**: 30 segundos para conexiones lentas
- **Anti-bloqueo**: User-Agent y opciones evasivas

---

## 📞 Contacto

- Instagram: @xonidu
- Facebook: xonidu
- Email: xonidu@gmail.com

---

**Licencia**: Uso educativo y personal. No comercial. Respeta términos de YouTube.
```
