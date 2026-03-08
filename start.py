#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XoniTube v5.5 - Buscador optimizado SIN MAXIMIZAR
Creado por Darian Alberto Camacho Salas
Para equipos de 1GB RAM - Ventana fija mediana
"""

import subprocess
import sys
import os

# ============================================================================
# CONFIGURACION OPTIMIZADA
# ============================================================================

REPRODUCTOR = "mpv"
TAMANO_VENTANA = "640x360"  # Tamaño fijo mediano (ni pequeño ni grande)
POSICION = "50%:50%"        # Centrado en pantalla

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
    Reproduccion con ventana de TAMAÑO FIJO (no maximizable)
    """
    print(f"\nReproduciendo en {nombre_calidad}...")
    print("  Tamaño fijo: 640x360 (ideal para 1GB RAM)")
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
        
        # MPV con opciones ANTI-LAG y ventana FIJA
        mpv_cmd = [
            REPRODUCTOR,
            "--cache=yes",
            "--cache-secs=15",           # Menos cache = menos RAM
            "--profile=fast",             # Perfil rápido
            "--vd-lavc-fast",              # Decodificación rápida
            "--vd-lavc-skip-loop-filter=all", # Saltar filtros
            "--no-sub",                     # Sin subtítulos
            "--no-osc",                      # Sin overlay
            "--no-osd-bar",                  # Sin barra OSD
            f"--geometry={TAMANO_VENTANA}",  # Tamaño fijo
            f"--geometry={POSICION}",        # Posición centrada
            "--ontop",                        # Siempre visible
            "--no-window-dragging",           # No arrastrar (ahorra CPU)
            "--no-border",                     # Sin bordes
            "--keepaspect-window",             # Mantener aspecto
            "--really-quiet",
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
    print("  1. Peor calidad (mas rapido, recomendado)")
    print("  2. 144p (muy baja)")
    print("  3. 240p (baja)")
    print("  4. 360p (media)")
    print("  5. 480p (estandar)")
    print("  6. 720p (HD - puede tener lag)") 
    print("  7. Solo audio")
    print("-"*50)
    print("Para 1GB RAM, recomendamos opciones 1-3")
    print("-"*50)
    
    while True:
        op = input("Elige una opcion (1-7, Enter=1): ").strip()
        
        if op == "":
            return "worst", "Peor calidad"
        
        calidades = {
            '1': ("worst", "Peor calidad"),
            '2': ("worst[height<=144]", "144p"),
            '3': ("worst[height<=240]", "240p"),
            '4': ("worst[height<=360]", "360p"),
            '5': ("worst[height<=480]", "480p"),
            '6': ("best[height<=720]", "720p HD"),
            '7': ("bestaudio", "Solo audio")
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
    print("XONITUBE v5.5 - MODO ANTI-LAG".center(70))
    print("="*70)
    print("Creado por Darian Alberto Camacho Salas".center(70))
    print("="*70)
    print("\nINSTRUCCIONES:")
    print("  • El video se abre en ventana MEDIANA (640x360)")
    print("  • NO maximices la ventana (causa lag y desincronizacion)")
    print("  • Si quieres ver mas grande, siéntate mas cerca")
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

