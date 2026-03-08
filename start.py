#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XoniTube v5.4 - Modo Framebuffer (sin X)
Creado por Darian Alberto Camacho Salas
"""

import subprocess
import sys
import os

def limpiar_pantalla():
    os.system('clear')

def buscar_videos(termino, cantidad):
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
                    'tit': titulo.strip()[:60],
                    'url': f"https://youtu.be/{vid.strip()}"
                })
        return videos
    except:
        return None

def mostrar_resultados(videos):
    print("\n" + "="*60)
    print("RESULTADOS".center(60))
    print("="*60)
    for v in videos:
        print(f"\n{v['num']}. {v['tit']}")
    print("\n" + "="*60)

def reproducir_fb(url, calidad):
    """Reproducción usando framebuffer (sin X)"""
    print(f"\nReproduciendo... (modo framebuffer)")
    print("Presiona Ctrl+C para volver\n")
    
    try:
        # Opción 1: Usar fbdev
        cmd = [
            "mpv",
            f"--vo=fbdev",  # Framebuffer directo
            "--ao=alsa",
            "--really-quiet",
            url
        ]
        subprocess.run(cmd)
        return True
    except:
        try:
            # Opción 2: Usar drm (más moderno)
            cmd = [
                "mpv",
                f"--vo=drm",
                "--ao=alsa",
                "--really-quiet",
                url
            ]
            subprocess.run(cmd)
            return True
        except:
            return False

def main():
    limpiar_pantalla()
    print("="*60)
    print("XONITUBE v5.4 - MODO FRAMEBUFFER".center(60))
    print("="*60)
    print("Creado por Darian Alberto Camacho Salas".center(60))
    print("="*60)
    
    while True:
        try:
            entrada = input("\nBuscar → ").strip()
            if entrada.lower() in ['salir', 'q']:
                break
            if not entrada:
                continue

            videos = buscar_videos(entrada, 5)
            if not videos:
                print("Sin resultados")
                continue

            mostrar_resultados(videos)
            sel = input("\nNúmero: ").strip()
            if sel.isdigit():
                idx = int(sel) - 1
                if 0 <= idx < len(videos):
                    print("\nCalidad: 1=Peor 2=144p 3=240p 4=Solo audio")
                    cal = input("Opción (Enter=1): ").strip()
                    calidades = {
                        '1': "worst",
                        '2': "worst[height<=144]",
                        '3': "worst[height<=240]",
                        '4': "bestaudio"
                    }
                    calidad = calidades.get(cal, "worst")
                    reproducir_fb(videos[idx]['url'], calidad)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
