#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XoniTube v4.2.2 - Buscador interactivo de YouTube
Creado por Darian Alberto Camacho Salas
"""

import subprocess
import sys
import os
import json
import time

# ============================================================================
# CONFIGURACION
# ============================================================================

CALIDAD_VIDEO = "worst"
REPRODUCTOR = "mpv"
TIMEOUT = 15  # segundos

# ============================================================================
# FUNCIONES
# ============================================================================

def limpiar_pantalla():
    """Limpia la pantalla"""
    os.system('clear' if os.name == 'posix' else 'cls')

def buscar_videos(termino, cantidad):
    """
    Busca videos en YouTube
    """
    print(f"\nBuscando {cantidad} videos: '{termino}'...")
    print("(esto puede tomar unos segundos)")
    
    try:
        cmd = [
            "yt-dlp",
            "--no-warnings",
            "--no-playlist",
            "--print-json",
            f"ytsearch{cantidad}:{termino}",
            "--sleep-interval", "0",
            "--max-sleep-interval", "0",
            "--geo-bypass",
            "--force-ipv4"
        ]
        
        resultado = subprocess.run(cmd, capture_output=True, text=True, timeout=TIMEOUT)
        
        if resultado.returncode != 0:
            print(f"Error en yt-dlp: {resultado.stderr[:100]}")
            return None
        
        videos = []
        for i, linea in enumerate(resultado.stdout.strip().split('\n'), 1):
            if linea:
                try:
                    data = json.loads(linea)
                    videos.append({
                        'numero': i,
                        'titulo': data.get('title', 'Sin titulo'),
                        'duracion': data.get('duration', 'N/A'),
                        'canal': data.get('channel', 'Desconocido'),
                        'link': f"https://youtube.com/watch?v={data.get('id', '')}"
                    })
                except json.JSONDecodeError:
                    continue
        
        if not videos:
            print("No se encontraron resultados")
            return None
            
        return videos
        
    except subprocess.TimeoutExpired:
        print(f"La busqueda tardo mas de {TIMEOUT} segundos")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None

def mostrar_videos(videos):
    """Muestra la lista de videos numerada"""
    print("\n" + "="*80)
    print("RESULTADOS".center(80))
    print("="*80)
    
    for v in videos:
        print(f"\n{v['numero']}. {v['titulo']}")
        print(f"   Canal: {v['canal']} | Duracion: {v['duracion']}s")
    print("\n" + "="*80)

def reproducir_video(link, titulo):
    """Reproduce un video"""
    print(f"\nReproduciendo: {titulo[:60]}...")
    print("Presiona Ctrl+C para volver al menu\n")
    
    try:
        cmd = [REPRODUCTOR, "--ytdl-format=" + CALIDAD_VIDEO, "--no-video", link]
        subprocess.run(cmd)
        return True
    except KeyboardInterrupt:
        print("\n\nReproduccion detenida")
        return True
    except Exception as e:
        print(f"Error al reproducir: {e}")
        return False

def preguntar_cantidad():
    """Pregunta cuantos resultados mostrar"""
    while True:
        try:
            cant = input("\nCuantos resultados quieres ver? (1-15, Enter para 5): ").strip()
            if cant == "":
                return 5
            cant = int(cant)
            if 1 <= cant <= 15:
                return cant
            else:
                print("Por favor ingresa un numero entre 1 y 15")
        except ValueError:
            print("Por favor ingresa un numero valido")

def preguntar_video(max_num):
    """Pregunta que video reproducir"""
    while True:
        try:
            opcion = input(f"\nQue video quieres reproducir? (1-{max_num}, Enter para volver): ").strip()
            if opcion == "":
                return None
            num = int(opcion)
            if 1 <= num <= max_num:
                return num
            else:
                print(f"Por favor ingresa un numero entre 1 y {max_num}")
        except ValueError:
            print("Por favor ingresa un numero valido")

def verificar_ytdlp():
    """Verifica que yt-dlp este instalado"""
    try:
        result = subprocess.run(["yt-dlp", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"yt-dlp version: {result.stdout.strip()}")
            return True
        else:
            print("yt-dlp no responde correctamente")
            return False
    except FileNotFoundError:
        print("yt-dlp no esta instalado")
        print("Instalalo con: sudo pacman -S yt-dlp (Arch)")
        print("o: sudo apt install yt-dlp (Ubuntu/Debian)")
        print("o: pip install yt-dlp")
        return False

# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

def main():
    """Funcion principal"""
    
    limpiar_pantalla()
    print("="*80)
    print("XONITUBE v4.2.2".center(80))
    print("="*80)
    print("Creado por Darian Alberto Camacho Salas".center(80))
    print("="*80)
    
    # Verificar yt-dlp
    verificar_ytdlp()
    
    print("\nINSTRUCCIONES:")
    print("  • Escribe SOLO lo que quieres buscar (sin la palabra 'buscar')")
    print("  • Ejemplo: sub_urban, kendrick lamar, musica relajante")
    print("  • Escribe 'salir' para terminar")
    print("-"*80)
    
    while True:
        try:
            # PASO 1: Preguntar busqueda
            busqueda = input("\nQue quieres buscar? → ").strip()
            
            if busqueda.lower() in ['salir', 'exit', 'q', 'quit']:
                print("\nHasta luego!")
                break
            
            if not busqueda:
                continue
            
            # PASO 2: Preguntar cantidad
            cantidad = preguntar_cantidad()
            
            # PASO 3: Buscar videos
            videos = buscar_videos(busqueda, cantidad)
            
            if not videos:
                print("\nNo se encontraron resultados. Intenta con otra busqueda.")
                continue
            
            # PASO 4: Mostrar resultados
            mostrar_videos(videos)
            
            # PASO 5: Preguntar cual reproducir
            while True:
                num = preguntar_video(len(videos))
                
                if num is None:
                    print("\nVolviendo al menu principal...")
                    break
                
                # PASO 6: Reproducir video seleccionado
                video = videos[num-1]
                reproducir_video(video['link'], video['titulo'])
                
                # PASO 7: Preguntar si quiere otro del mismo resultado
                otro = input("\nQuieres reproducir otro video de esta busqueda? (s/n): ").strip().lower()
                if otro not in ['s', 'si', 'y', 'yes', '']:
                    break
            
        except KeyboardInterrupt:
            print("\n\nHasta luego!")
            break
        except Exception as e:
            print(f"\nError inesperado: {e}")
            print("Continuando...")

# ============================================================================
# PUNTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nError fatal: {e}")
        sys.exit(1)
