#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XoniTube v5.3 - Buscador de YouTube ULTRA OPTIMIZADO
Creado por Darian Alberto Camacho Salas
Para xoniant32 - Máximo rendimiento en 1GB RAM
"""

import subprocess
import sys
import os

# ============================================================================
# CONFIGURACION OPTIMIZADA
# ============================================================================

REPRODUCTOR = "mpv"
BACKEND_VIDEO = "x11"  # El más compatible

# ============================================================================
# FUNCIONES PRINCIPALES
# ============================================================================

def limpiar_pantalla():
    os.system('clear' if os.name == 'posix' else 'cls')

def buscar_videos(termino, cantidad):
    """Busqueda ultra rápida"""
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
        resultado = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        if resultado.returncode != 0:
            return None
        videos = []
        for linea in resultado.stdout.strip().split('\n'):
            if '|' in linea:
                titulo, vid = linea.split('|', 1)
                videos.append({
                    'num': len(videos) + 1,
                    'tit': titulo.strip()[:60],
                    'url': f"https://youtu.be/{vid.strip()}"
                })
        return videos if videos else None
    except:
        return None

def mostrar_resultados(videos):
    print("\n" + "="*60)
    print("RESULTADOS".center(60))
    print("="*60)
    for v in videos:
        print(f"\n{v['num']}. {v['tit']}")
    print("\n" + "="*60)

def reproducir(url, calidad):
    """
    Reproducción ULTRA OPTIMIZADA - Mínimo consumo de recursos
    """
    print(f"\nReproduciendo... (calidad {calidad})")
    print("Presiona Ctrl+C para volver\n")
    print("CONTROLES: ← → Space ↑ ↓ q")
    print("-"*40)

    try:
        # yt-dlp optimizado
        cmd_yt = [
            "yt-dlp",
            "-f", calidad,
            "-o", "-",
            "--quiet",
            "--no-part",
            "--buffer-size", "16K",        # Buffer pequeño
            "--http-chunk-size", "500K",    # Chunks pequeños
            url
        ]

        # mpv OPTIMIZADO PARA RENDIMIENTO
        cmd_mpv = [
            REPRODUCTOR,
            f"--vo={BACKEND_VIDEO}",
            "--ao=alsa",
            "--cache=no",                    # Sin caché (menos RAM)
            "--profile=fast",                 # Perfil rápido
            "--vd-lavc-fast",                 # Decodificación rápida
            "--vd-lavc-skip-loop-filter=all", # Saltar filtros pesados
            "--no-sub",                        # Sin subtítulos
            "--no-osc",                        # Sin overlay (menos CPU)
            "--no-osd-bar",                    # Sin barra OSD
            "--really-quiet",
            "--ontop",                         # Siempre visible
            "--geometry=50%x50%",              # Ventana más pequeña (menos píxeles)
            "--window-minimized=no",
            "-"
        ]

        p1 = subprocess.Popen(cmd_yt, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        p2 = subprocess.Popen(cmd_mpv, stdin=p1.stdout)
        p2.wait()
        return True

    except KeyboardInterrupt:
        print("\n\nDetenido")
        return True
    except Exception as e:
        print(f"\nError: {e}")
        return False

def preguntar_cantidad():
    try:
        cant = input("\nCuantos? (1-10, Enter=5): ").strip()
        if cant == "":
            return 5
        cant = int(cant)
        if 1 <= cant <= 10:
            return cant
        return 5
    except:
        return 5

def preguntar_calidad():
    """Calidades optimizadas para bajo consumo"""
    print("\nCALIDAD (menor número = más rápido):")
    print("  1. Peor (muy rápida)")
    print("  2. 144p (rápida)")
    print("  3. 240p")
    print("  4. 360p")
    print("  5. Solo audio")
    op = input("\nElige (1-5, Enter=1): ").strip()
    
    calidades = {
        '1': "worst",
        '2': "worst[height<=144]",
        '3': "worst[height<=240]",
        '4': "worst[height<=360]",
        '5': "bestaudio"
    }
    return calidades.get(op, "worst")

# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

def main():
    limpiar_pantalla()
    print("="*60)
    print("XONITUBE v5.3 - MODO RÁPIDO".center(60))
    print("="*60)
    print("Creado por Darian Alberto Camacho Salas".center(60))
    print("="*60)
    print("\nBusca un video y listo!")
    print("(sin lags, optimizado para 1GB RAM)")

    while True:
        try:
            entrada = input("\nBuscar → ").strip()
            if entrada.lower() in ['salir', 'q']:
                break
            if not entrada:
                continue

            cantidad = preguntar_cantidad()
            videos = buscar_videos(entrada, cantidad)
            
            if not videos:
                print("\nSin resultados")
                continue

            mostrar_resultados(videos)

            while True:
                sel = input("\nNúmero (Enter nueva búsqueda): ").strip()
                if sel == "":
                    break
                if sel.isdigit():
                    idx = int(sel) - 1
                    if 0 <= idx < len(videos):
                        calidad = preguntar_calidad()
                        reproducir(videos[idx]['url'], calidad)
                        otro = input("\nOtro video? (s/n): ").strip().lower()
                        if otro not in ['s', 'si']:
                            break
                    else:
                        print(f"Número 1-{len(videos)}")
                else:
                    print("Número inválido")

        except KeyboardInterrupt:
            print("\n\nHasta luego!")
            break

if __name__ == "__main__":
    try:
        main()
    except:
        pass
