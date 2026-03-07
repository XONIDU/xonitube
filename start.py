#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XoniTube v5.1 - Buscador de YouTube con visualización forzada
Creado por Darian Alberto Camacho Salas
Para xoniant32 - Garantiza que el video SE VEA.
"""

import subprocess
import sys
import os
import time

# ============================================================================
# CONFIGURACIÓN
# ============================================================================

REPRODUCTOR = "mpv"
CALIDAD_POR_DEFECTO = "worst"
BACKEND_VIDEO_PREFERIDO = "x11"  # Intenta primero con X11
BACKENDS_ALTERNOS = ["sdl", "vaapi", "vdpau", "drm", "xv"]  # Opciones de respaldo

# ============================================================================
# FUNCIONES PRINCIPALES
# ============================================================================

def limpiar_pantalla():
    os.system('clear' if os.name == 'posix' else 'cls')

def buscar_videos(termino, cantidad):
    """Busca videos usando yt-dlp de forma ultra rápida"""
    print(f"\nBuscando: '{termino}'...")
    try:
        cmd = [
            "yt-dlp",
            "--no-warnings",
            "--quiet",
            "--flat-playlist",
            "--print", "%(title)s|%(id)s",
            f"ytsearch{cantidad}:{termino}"
        ]
        resultado = subprocess.run(cmd, capture_output=True, text=True)
        if resultado.returncode != 0:
            return None
        videos = []
        for linea in resultado.stdout.strip().split('\n'):
            if '|' in linea:
                titulo, vid = linea.split('|', 1)
                videos.append({
                    'num': len(videos) + 1,
                    'tit': titulo.strip()[:70],
                    'url': f"https://youtu.be/{vid.strip()}"
                })
        return videos if videos else None
    except:
        return None

def mostrar_resultados(videos):
    print("\n" + "="*70)
    print("RESULTADOS".center(70))
    print("="*70)
    for v in videos:
        print(f"\n{v['num']}. {v['tit']}")
    print("\n" + "="*70)

def probar_backend_video(backend):
    """Prueba si un backend de video funciona (reproducción silenciosa de 1 frame)"""
    try:
        cmd = [
            REPRODUCTOR,
            f"--vo={backend}",
            "--ao=null",        # Sin audio
            "--frames=1",       # Solo 1 frame
            "--really-quiet",
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        ]
        subprocess.run(cmd, timeout=5, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        return True
    except:
        return False

def reproducir_con_fallback(url, calidad, nombre_calidad):
    """
    Intenta reproducir con el backend preferido; si falla, prueba alternativas.
    """
    # Lista de backends a probar: preferido + alternativos
    backends_a_probar = [BACKEND_VIDEO_PREFERIDO] + BACKENDS_ALTERNOS

    for backend in backends_a_probar:
        print(f"Probando backend de video: {backend} ...")
        if probar_backend_video(backend):
            print(f"Usando backend: {backend}")
            break
    else:
        print("\n¡No se encontró ningún backend de video funcional!")
        print("Instala controladores de video: 'sudo apt install xserver-xorg-video-intel' (o el correspondiente a tu GPU).")
        return False

    print(f"\n▶ Reproduciendo en {nombre_calidad} (backend {backend})...")
    print("Presiona Ctrl+C para volver al menú\n")
    print("CONTROLES MPV:")
    print("  ← → : Retroceder/Avanzar 5s")
    print("  Space : Pausa")
    print("  ↑ ↓ : Volumen")
    print("  q : Salir")
    print("-"*50)

    try:
        cmd_yt = [
            "yt-dlp",
            "-f", calidad,
            "-o", "-",
            "--quiet",
            url
        ]

        cmd_mpv = [
            REPRODUCTOR,
            f"--vo={backend}",
            "--ao=alsa",         # Forzar ALSA (evita pipewire)
            "--cache=yes",
            "--cache-secs=30",
            "--x11-bypass-compositor=yes",  # Evita problemas con compositores
            "--window-minimized=no",         # Asegura que la ventana no se minimice
            "--keepaspect-window",
            "--really-quiet",
            "-"
        ]

        p1 = subprocess.Popen(cmd_yt, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        p2 = subprocess.Popen(cmd_mpv, stdin=p1.stdout)
        p2.wait()
        return True

    except KeyboardInterrupt:
        print("\n\nReproduccion detenida")
        return True
    except Exception as e:
        print(f"\nError al reproducir con backend {backend}: {e}")
        return False

def preguntar_cantidad():
    while True:
        try:
            cant = input("\nCuantos resultados? (1-15, Enter=5): ").strip()
            if cant == "":
                return 5
            cant = int(cant)
            if 1 <= cant <= 15:
                return cant
            print("Numero entre 1 y 15")
        except ValueError:
            print("Ingresa un numero valido")

def preguntar_calidad():
    print("\n" + "="*50)
    print("CALIDADES DISPONIBLES".center(50))
    print("="*50)
    print("  1. Peor calidad (mas rapida, ahorro de datos)")
    print("  2. 144p (muy baja)")
    print("  3. 240p (baja)")
    print("  4. 360p (media)")
    print("  5. 480p (estandar)")
    print("  6. 720p (HD)")
    print("  7. 1080p (Full HD)")
    print("  8. Mejor calidad disponible (mas lenta)")
    print("  9. Solo audio (sin video)")
    print("-"*50)

    while True:
        op = input("Elige una opcion (1-9, Enter=1): ").strip()
        if op == "":
            return "worst", "Peor calidad"
        calidades = {
            '1': ("worst", "Peor calidad"),
            '2': ("worst[height<=144]", "144p"),
            '3': ("worst[height<=240]", "240p"),
            '4': ("worst[height<=360]", "360p"),
            '5': ("worst[height<=480]", "480p"),
            '6': ("best[height<=720]", "720p HD"),
            '7': ("best[height<=1080]", "1080p Full HD"),
            '8': ("best", "Mejor calidad"),
            '9': ("bestaudio", "Solo audio")
        }
        if op in calidades:
            return calidades[op]
        print("Opcion no valida")

# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

def main():
    limpiar_pantalla()
    print("="*70)
    print("XONITUBE v5.1 - MODO VIDEO FORZADO".center(70))
    print("="*70)
    print("Creado por Darian Alberto Camacho Salas".center(70))
    print("="*70)
    print("\nINSTRUCCIONES:")
    print("  • Escribe lo que quieres buscar (ej: 'kendrick lamar')")
    print("  • El video se FORZARÁ a mostrarse con el mejor backend disponible.")
    print("  • Si aún no ves video, instala controladores: 'sudo apt install xserver-xorg-video-intel'")
    print("="*70)

    while True:
        try:
            entrada = input("\nBuscar → ").strip()
            if entrada.lower() in ['salir', 'exit', 'q']:
                print("\nHasta luego!")
                break
            if not entrada:
                continue

            cantidad = preguntar_cantidad()
            videos = buscar_videos(entrada, cantidad)
            if not videos:
                print("\nNo se encontraron resultados")
                continue

            mostrar_resultados(videos)

            while True:
                sel = input("\nNumero de video (Enter para nueva busqueda): ").strip()
                if sel == "":
                    break
                if sel.isdigit():
                    idx = int(sel) - 1
                    if 0 <= idx < len(videos):
                        formato, nombre_calidad = preguntar_calidad()
                        # Intentar reproducir con fallback automático
                        reproducir_con_fallback(videos[idx]['url'], formato, nombre_calidad)
                        otro = input("\nReproducir otro video de esta busqueda? (s/n): ").strip().lower()
                        if otro not in ['s', 'si', 'y']:
                            break
                    else:
                        print(f"Numero debe ser entre 1 y {len(videos)}")
                else:
                    print("Ingresa un numero valido")

        except KeyboardInterrupt:
            print("\n\nHasta luego!")
            break
        except Exception as e:
            print(f"\nError inesperado: {e}")

if __name__ == "__main__":
    main()
