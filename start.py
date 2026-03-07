#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XoniTube v5.0 - Buscador ultra optimizado
Creado por Darian Alberto Camacho Salas
Consumo minimo de recursos - Sin limites de tiempo
"""

import subprocess
import sys
import os
import signal

# ============================================================================
# CONFIGURACION OPTIMIZADA
# ============================================================================

REPRODUCTOR = "mpv"

# ============================================================================
# FUNCIONES ULTRA RAPIDAS
# ============================================================================

def limpiar_pantalla():
    """Limpia la pantalla"""
    os.system('clear' if os.name == 'posix' else 'cls')

def buscar_videos(termino, cantidad):
    """
    Busqueda simple y rapida - sin timeouts
    """
    print(f"\nBuscando: '{termino}'...")
    
    try:
        # Comando simple
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
        
        return videos if videos else None
        
    except Exception as e:
        return None

def mostrar_resultados(videos):
    """Muestra resultados"""
    print("\n" + "-"*50)
    for v in videos:
        print(f"{v['num']}. {v['tit']}")
    print("-"*50)

def reproducir(url, calidad):
    """
    Reproduccion simple
    """
    print(f"\nReproduciendo...")
    print("Ctrl+C para volver\n")
    
    try:
        # Streaming directo
        cmd = [
            "yt-dlp",
            "-f", calidad,
            "-o", "-",
            "--quiet",
            url
        ]
        
        mpv_cmd = [
            REPRODUCTOR,
            "--cache=yes",
            "--profile=fast",
            "-"
        ]
        
        p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        p2 = subprocess.Popen(mpv_cmd, stdin=p1.stdout)
        p2.wait()
        
        return True
        
    except KeyboardInterrupt:
        print("\n\nDetenido")
        return True
    except:
        return False

def preguntar_cantidad():
    """Pregunta simple"""
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
    """Seleccion simple de calidad"""
    print("\nCalidad: 1=P 2=144 3=240 4=360 5=480 6=Mejor 7=Audio")
    op = input("→ ").strip()
    
    calidades = {
        '1': "worst",
        '2': "worst[height<=144]",
        '3': "worst[height<=240]",
        '4': "worst[height<=360]",
        '5': "worst[height<=480]",
        '6': "best",
        '7': "bestaudio"
    }
    return calidades.get(op, "worst")

# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

def main():
    """Funcion principal"""
    
    limpiar_pantalla()
    print("="*50)
    print("XONITUBE v5.0".center(50))
    print("="*50)
    print("Creado por Darian Alberto Camacho Salas".center(50))
    print("="*50)
    print("\nModo simple - Sin limites de tiempo")
    print("Escribe lo que quieres buscar")
    print("'salir' para terminar")
    
    while True:
        try:
            entrada = input("\n> ").strip()
            
            if entrada.lower() in ['salir', 'q', 'exit']:
                print("\nHasta luego!")
                break
            
            if not entrada:
                continue
            
            # Buscar
            cantidad = preguntar_cantidad()
            videos = buscar_videos(entrada, cantidad)
            
            if not videos:
                print("Sin resultados")
                continue
            
            # Mostrar
            mostrar_resultados(videos)
            
            # Seleccionar
            sel = input("\nNumero? (Enter para nueva busqueda): ").strip()
            
            if sel and sel.isdigit():
                idx = int(sel) - 1
                if 0 <= idx < len(videos):
                    calidad = preguntar_calidad()
                    reproducir(videos[idx]['url'], calidad)
                    
        except KeyboardInterrupt:
            print("\n\nHasta luego!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    try:
        main()
    except:
        pass
