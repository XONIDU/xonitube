#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XoniTube v5.2 - Buscador de YouTube con ventana siempre visible
Creado por Darian Alberto Camacho Salas
Para xoniant32 - Ventana siempre encima y en grande
"""

import subprocess
import sys
import os
import time

# ============================================================================
# CONFIGURACION
# ============================================================================

REPRODUCTOR = "mpv"
CALIDAD_POR_DEFECTO = "worst"
BACKEND_VIDEO = "x11"  # Backend fijo para maxima compatibilidad

# ============================================================================
# FUNCIONES PRINCIPALES
# ============================================================================

def limpiar_pantalla():
    """Limpia la pantalla de la terminal"""
    os.system('clear' if os.name == 'posix' else 'cls')

def buscar_videos(termino, cantidad):
    """
    Busca videos en YouTube usando yt-dlp de forma rapida y liviana
    """
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

    except Exception as e:
        return None

def mostrar_resultados(videos):
    """Muestra la lista de resultados numerados"""
    print("\n" + "="*70)
    print("RESULTADOS".center(70))
    print("="*70)
    for v in videos:
        print(f"\n{v['num']}. {v['tit']}")
    print("\n" + "="*70)

def reproducir(url, calidad, nombre_calidad):
    """
    Reproduce el video usando mpv con ventana siempre encima y en grande
    """
    print(f"\nReproduciendo en {nombre_calidad} (backend {BACKEND_VIDEO})...")
    print("Presiona Ctrl+C para volver al menu\n")
    print("CONTROLES MPV:")
    print("  ← → : Retroceder/Avanzar 5s")
    print("  Space : Pausa")
    print("  ↑ ↓ : Volumen")
    print("  f : Pantalla completa")
    print("  q : Salir")
    print("-"*50)

    try:
        # Comando yt-dlp para obtener el stream y pasarlo por pipe
        cmd_yt = [
            "yt-dlp",
            "-f", calidad,
            "-o", "-",
            "--quiet",
            url
        ]

        # Comando mpv con opciones para ventana siempre encima y en grande
        cmd_mpv = [
            REPRODUCTOR,
            f"--vo={BACKEND_VIDEO}",
            "--ao=alsa",         # Forzar ALSA (evita pipewire)
            "--cache=yes",
            "--cache-secs=30",
            "--x11-bypass-compositor=yes",  # Evita problemas con compositores
            "--window-minimized=no",         # Asegura que la ventana no se minimice
            "--keepaspect-window",
            "--geometry=100%x100%",          # Ocupa toda la pantalla
            "--ontop",                        # Siempre encima de todo
            "--ontop-level=window",           # Nivel de prioridad
            "--focus-on-open=yes",            # Enfocar al abrir
            "--really-quiet",
            "-"
        ]

        # Ejecutar procesos
        p1 = subprocess.Popen(cmd_yt, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        p2 = subprocess.Popen(cmd_mpv, stdin=p1.stdout)
        p2.wait()

        return True

    except KeyboardInterrupt:
        print("\n\nReproduccion detenida")
        return True
    except Exception as e:
        print(f"\nError al reproducir: {e}")
        return False

def preguntar_cantidad():
    """Pregunta al usuario cuantos resultados desea ver"""
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
    """Muestra menu de calidades y retorna el formato y nombre elegido"""
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
    """Flujo principal del programa"""
    limpiar_pantalla()
    print("="*70)
    print("XONITUBE v5.2".center(70))
    print("="*70)
    print("Creado por Darian Alberto Camacho Salas".center(70))
    print("="*70)
    print("\nINSTRUCCIONES:")
    print("  • Escribe lo que quieres buscar (ej: 'kendrick lamar')")
    print("  • Responde las preguntas para elegir cantidad y calidad")
    print("  • El video se abrira en pantalla completa y siempre visible")
    print("  • Durante la reproduccion usa ← → Space ↑ ↓ f q")
    print("  • Escribe 'salir' para terminar")
    print("="*70)

    while True:
        try:
            entrada = input("\nBuscar → ").strip()

            if entrada.lower() in ['salir', 'exit', 'q']:
                print("\nHasta luego!")
                break

            if not entrada:
                continue

            # 1. Preguntar cantidad de resultados
            cantidad = preguntar_cantidad()

            # 2. Realizar busqueda
            videos = buscar_videos(entrada, cantidad)

            if not videos:
                print("\nNo se encontraron resultados")
                continue

            # 3. Mostrar resultados
            mostrar_resultados(videos)

            # 4. Bucle para seleccionar y reproducir videos de esta busqueda
            while True:
                sel = input("\nNumero de video (Enter para nueva busqueda): ").strip()

                if sel == "":
                    break

                if sel.isdigit():
                    idx = int(sel) - 1
                    if 0 <= idx < len(videos):
                        # 5. Elegir calidad
                        formato, nombre_calidad = preguntar_calidad()

                        # 6. Reproducir
                        reproducir(videos[idx]['url'], formato, nombre_calidad)

                        # 7. Preguntar si desea otro de la misma busqueda
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
            # En caso de error, volvemos al inicio del bucle

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nError fatal: {e}")
        sys.exit(1)
