#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XoniTube v5.6 - Buscador con ventana NO maximizable
Creado por Darian Alberto Camacho Salas
Solucion: ventana fija para evitar lag al maximizar
"""

import subprocess
import sys
import os

# ============================================================================
# CONFIGURACION
# ============================================================================

REPRODUCTOR = "mpv"
TAMANO_VENTANA = "640x360"  # Tamaño fijo que funciona bien

# ============================================================================
# FUNCIONES
# ============================================================================

def limpiar_pantalla():
    os.system('clear' if os.name == 'posix' else 'cls')

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
                    'tit': titulo.strip()[:70],
                    'url': f"https://youtu.be/{vid.strip()}"
                })
        return videos if videos else None
    except Exception as e:
        return None

def mostrar_resultados(videos):
    print("\n" + "="*70)
    print("RESULTADOS".center(70))
    print("="*70)
    for v in videos:
        print(f"\n{v['num']}. {v['tit']}")
    print("\n" + "="*70)

def reproducir(url, calidad, nombre_calidad):
    """
    Reproduccion con ventana de tamaño fijo
    """
    print(f"\nReproduciendo en {nombre_calidad}...")
    print("  Tamaño fijo: 640x360 (NO maximizar - causa lag)")
    print("  Presiona Ctrl+C para volver al menu\n")
    print("  CONTROLES MPV:")
    print("    ← → : Retroceder/Avanzar 5s")
    print("    Space : Pausa")
    print("    ↑ ↓ : Volumen")
    print("    q : Salir")
    print("-"*50)
    
    try:
        cmd_yt = [
            "yt-dlp",
            "-f", calidad,
            "-o", "-",
            "--quiet",
            url
        ]
        
        # MPV con tamaño fijo y opciones que evitan maximizar
        mpv_cmd = [
            REPRODUCTOR,
            "--cache=yes",
            "--cache-secs=30",
            "--no-window-dragging",        # Evita redimensionar
            "--no-border",                  # Sin bordes para no tentar a maximizar
            "--geometry", TAMANO_VENTANA,   # Tamaño fijo
            "--ontop",                       # Siempre visible
            "--keepaspect-window",           # Mantener aspecto
            "-"
        ]
        
        p1 = subprocess.Popen(cmd_yt, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        p2 = subprocess.Popen(mpv_cmd, stdin=p1.stdout)
        p2.wait()
        
        return True
        
    except KeyboardInterrupt:
        print("\n\nReproduccion detenida")
        return True
    except Exception as e:
        print(f"\nError: {e}")
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
            print("Por favor ingresa un numero entre 1 y 15")
        except ValueError:
            print("Numero invalido")

def preguntar_calidad():
    print("\n" + "="*50)
    print("CALIDADES DISPONIBLES".center(50))
    print("="*50)
    print("  1. Peor calidad (mas rapido, ahorro de datos)")
    print("  2. 144p (muy baja)")
    print("  3. 240p (baja)")
    print("  4. 360p (media)")
    print("  5. 480p (estandar)")
    print("  6. 720p (HD)") 
    print("  7. 1080p (Full HD)")
    print("  8. Mejor calidad disponible (mas lento)")
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
        
        print("Opcion invalida")

# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

def main():
    limpiar_pantalla()
    print("="*70)
    print("XONITUBE v5.6 - MODO VENTANA FIJA".center(70))
    print("="*70)
    print("Creado por Darian Alberto Camacho Salas".center(70))
    print("="*70)
    print("\nINSTRUCCIONES:")
    print("  • El video se abre en ventana de 640x360 (tamaño fijo)")
    print("  • IMPORTANTE: No maximices la ventana o tendras lag")
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
                        reproducir(videos[idx]['url'], formato, nombre_calidad)
                        
                        otro = input("\nReproducir otro video de esta busqueda? (s/n): ").strip().lower()
                        if otro not in ['s', 'si', 'y']:
                            break
                    else:
                        print(f"Numero debe ser entre 1 y {len(videos)}")
                else:
                    print("Por favor ingresa un numero valido")
                    
        except KeyboardInterrupt:
            print("\n\nHasta luego!")
            break
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nError fatal: {e}")
