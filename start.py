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

# ============================================================================
# CONFIGURACION OPTIMIZADA
# ============================================================================

REPRODUCTOR = "mpv"

# ============================================================================
# FUNCIONES
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
    """Muestra resultados"""
    print("\n" + "="*70)
    print("RESULTADOS".center(70))
    print("="*70)
    for v in videos:
        print(f"\n{v['num']}. {v['tit']}")
    print("\n" + "="*70)

def reproducir(url, calidad, nombre_calidad):
    """
    Reproduccion simple
    """
    print(f"\n▶ Reproduciendo en {nombre_calidad}...")
    print("  Presiona Ctrl+C para volver al menu\n")
    print("  CONTROLES MPV:")
    print("    ← → : Retroceder/Avanzar 5s")
    print("    Space : Pausa")
    print("    ↑ ↓ : Volumen")
    print("    q : Salir")
    print("-"*50)
    
    try:
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
            "--cache-secs=30",
            "-"
        ]
        
        p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        p2 = subprocess.Popen(mpv_cmd, stdin=p1.stdout)
        p2.wait()
        
        return True
        
    except KeyboardInterrupt:
        print("\n\n⏹ Reproduccion detenida")
        return True
    except Exception as e:
        print(f"\nError: {e}")
        return False

def preguntar_cantidad():
    """Pregunta simple"""
    while True:
        try:
            cant = input("\n¿Cuantos resultados? (1-15, Enter=5): ").strip()
            if cant == "":
                return 5
            cant = int(cant)
            if 1 <= cant <= 15:
                return cant
            print("Por favor ingresa un numero entre 1 y 15")
        except ValueError:
            print("Numero invalido")

def preguntar_calidad():
    """Seleccion de calidad con texto claro"""
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
    """Funcion principal"""
    
    limpiar_pantalla()
    print("="*70)
    print("XONITUBE v5.0".center(70))
    print("="*70)
    print("Creado por Darian Alberto Camacho Salas".center(70))
    print("="*70)
    print("\nINSTRUCCIONES:")
    print("  • Escribe lo que quieres buscar")
    print("  • Ejemplo: r u mine, kendrick lamar, bad bunny")
    print("  • Escribe 'salir' para terminar")
    print("="*70)
    
    while True:
        try:
            entrada = input("\n🔍 Buscar → ").strip()
            
            if entrada.lower() in ['salir', 'exit', 'q']:
                print("\n👋 Hasta luego!")
                break
            
            if not entrada:
                continue
            
            # Preguntar cantidad
            cantidad = preguntar_cantidad()
            
            # Buscar videos
            videos = buscar_videos(entrada, cantidad)
            
            if not videos:
                print("\n❌ No se encontraron resultados")
                continue
            
            # Mostrar resultados
            mostrar_resultados(videos)
            
            # Seleccionar video
            while True:
                sel = input("\n🎯 Numero de video (Enter para nueva busqueda): ").strip()
                
                if sel == "":
                    break
                
                if sel.isdigit():
                    idx = int(sel) - 1
                    if 0 <= idx < len(videos):
                        # Preguntar calidad
                        formato, nombre_calidad = preguntar_calidad()
                        
                        # Reproducir
                        reproducir(videos[idx]['url'], formato, nombre_calidad)
                        
                        # Preguntar si otro del mismo resultado
                        otro = input("\n❓ Reproducir otro video de esta busqueda? (s/n): ").strip().lower()
                        if otro not in ['s', 'si', 'y']:
                            break
                    else:
                        print(f"Numero debe ser entre 1 y {len(videos)}")
                else:
                    print("Por favor ingresa un numero valido")
                    
        except KeyboardInterrupt:
            print("\n\n👋 Hasta luego!")
            break
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nError fatal: {e}")
