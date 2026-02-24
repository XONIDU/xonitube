#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XoniTube v4.2.0 - Buscador de YouTube
Creado por Darian Alberto Camacho Salas
Con metodo anti-bloqueo por defecto y autolimpieza
"""

import subprocess
import sys
import os
import tempfile
import atexit
import signal

# ============================================================================
# CONFIGURACION
# ============================================================================

REPRODUCTOR = "mpv"
USAR_YTDLP_POR_DEFECTO = True  # Usar metodo anti-bloqueo siempre
ARCHIVOS_TEMP = []  # Lista para rastrear archivos temporales

# ============================================================================
# FUNCIONES DE LIMPIEZA
# ============================================================================

def limpiar_archivos_temp():
    """Elimina todos los archivos temporales creados"""
    for archivo in ARCHIVOS_TEMP:
        try:
            if os.path.exists(archivo):
                os.unlink(archivo)
        except:
            pass

def signal_handler(sig, frame):
    """Maneja señales como Ctrl+C"""
    limpiar_archivos_temp()
    print("\n\nHasta luego!")
    sys.exit(0)

# Registrar limpieza al salir
atexit.register(limpiar_archivos_temp)
signal.signal(signal.SIGINT, signal_handler)

# ============================================================================
# FUNCIONES PRINCIPALES
# ============================================================================

def limpiar_pantalla():
    """Limpia la pantalla"""
    os.system('clear' if os.name == 'posix' else 'cls')

def buscar_videos(termino, cantidad):
    """
    Busca videos en YouTube
    """
    print(f"\nBuscando: '{termino}'...")
    
    try:
        cmd = [
            "yt-dlp",
            "--no-warnings",
            "--get-title",
            "--get-id",
            f"ytsearch{cantidad}:{termino}"
        ]
        
        resultado = subprocess.run(cmd, capture_output=True, text=True)
        
        if resultado.returncode != 0:
            print(f"Error en busqueda")
            return None
        
        lineas = resultado.stdout.strip().split('\n')
        videos = []
        
        for i in range(0, len(lineas), 2):
            if i + 1 < len(lineas):
                titulo = lineas[i].strip()
                video_id = lineas[i+1].strip()
                
                videos.append({
                    'numero': len(videos) + 1,
                    'titulo': titulo,
                    'link': f"https://youtube.com/watch?v={video_id}"
                })
        
        return videos if videos else None
        
    except Exception as e:
        print(f"Error: {e}")
        return None

def mostrar_videos(videos):
    """Muestra la lista de videos"""
    print("\n" + "="*70)
    print("RESULTADOS".center(70))
    print("="*70)
    
    for v in videos:
        print(f"\n{v['numero']}. {v['titulo']}")
    print("\n" + "="*70)

def mostrar_calidades():
    """Muestra las opciones de calidad"""
    print("\nCALIDADES DISPONIBLES:")
    print("  1. Peor calidad (mas rapido)")
    print("  2. 144p")
    print("  3. 240p")
    print("  4. 360p")
    print("  5. 480p")
    print("  6. Mejor calidad (mas lento)")
    print("  7. Solo audio")

def obtener_formato_calidad(opcion):
    """Convierte opcion a formato yt-dlp"""
    formatos = {
        '1': "worst",
        '2': "worst[height<=144]",
        '3': "worst[height<=240]",
        '4': "worst[height<=360]",
        '5': "worst[height<=480]",
        '6': "best",
        '7': "bestaudio"
    }
    return formatos.get(opcion, "worst")

def preguntar_calidad():
    """Pregunta que calidad usar"""
    while True:
        mostrar_calidades()
        opcion = input("\nElige calidad (1-7, Enter=1): ").strip()
        
        if opcion == "":
            return "worst"
        
        if opcion in ['1','2','3','4','5','6','7']:
            return obtener_formato_calidad(opcion)
        
        print("Opcion invalida")

def reproducir_video(link, titulo, formato_calidad):
    """Reproduce un video con metodo anti-bloqueo y autolimpieza"""
    calidad_texto = {
        "worst": "Peor calidad",
        "worst[height<=144]": "144p",
        "worst[height<=240]": "240p",
        "worst[height<=360]": "360p",
        "worst[height<=480]": "480p",
        "best": "Mejor calidad",
        "bestaudio": "Solo audio"
    }.get(formato_calidad, formato_calidad)
    
    print(f"\nReproduciendo: {titulo[:50]}...")
    print(f"Calidad: {calidad_texto}")
    print("Metodo: anti-bloqueo (streaming sin guardar archivos)")
    print("\nCONTROLES MPV:")
    print("  ← →  : Retroceder / Avanzar 5 segundos")
    print("  ↑ ↓  : Subir / Bajar volumen")
    print("  Space: Pausa/Reanudar")
    print("  q    : Salir de la reproduccion")
    print("  Ctrl+C: Volver al menu\n")
    
    try:
        # Usar pipe - NO crea archivos en disco
        cmd_ytdlp = [
            "yt-dlp",
            "-f", formato_calidad,
            "-o", "-",  # Salida a stdout (pipe, no archivo)
            "--no-part",  # No usar archivos parciales
            "--no-mtime",  # No modificar tiempos
            link
        ]
        
        cmd_mpv = [
            REPRODUCTOR,
            "--cache=yes",
            "--cache-secs=30",
            "--demuxer-max-bytes=150M",
            "--demuxer-readahead-secs=20",
            "--no-input-default-bindings",
            "--input-conf=/dev/null",  # Evitar archivos de config
            "-"  # Entrada desde stdin
        ]
        
        # Ejecutar sin crear archivos temporales
        p1 = subprocess.Popen(
            cmd_ytdlp, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL
        )
        
        p2 = subprocess.Popen(
            cmd_mpv, 
            stdin=p1.stdout,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        
        p2.wait()  # Esperar a que termine la reproduccion
        
        # Asegurar que el pipe se cierre correctamente
        if p1.stdout:
            p1.stdout.close()
        
        return True
        
    except KeyboardInterrupt:
        print("\n\nReproduccion detenida")
        # Terminar procesos hijos si existen
        try:
            p1.terminate()
            p2.terminate()
        except:
            pass
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def preguntar_cantidad():
    """Pregunta cuantos resultados"""
    while True:
        try:
            cant = input("\nCuantos resultados? (1-10, Enter=5): ").strip()
            if cant == "":
                return 5
            cant = int(cant)
            if 1 <= cant <= 10:
                return cant
            print("Numero entre 1 y 10")
        except ValueError:
            print("Numero invalido")

def preguntar_video(max_num):
    """Pregunta que video reproducir"""
    while True:
        try:
            opcion = input(f"\nQue video? (1-{max_num}, Enter=menu): ").strip()
            if opcion == "":
                return None
            num = int(opcion)
            if 1 <= num <= max_num:
                return num
            print(f"Numero entre 1 y {max_num}")
        except ValueError:
            print("Numero invalido")

# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

def main():
    """Funcion principal"""
    
    limpiar_pantalla()
    print("="*70)
    print("XONITUBE v4.2.0".center(70))
    print("="*70)
    print("Creado por Darian Alberto Camacho Salas".center(70))
    print("="*70)
    print("\nINFORMACION:")
    print("  • Metodo anti-bloqueo activado por defecto")
    print("  • Streaming directo - No guarda archivos en disco")
    print("  • Usa ← → para retroceder/avanzar durante reproduccion")
    print("  • Space para pausar")
    
    while True:
        try:
            # Busqueda
            busqueda = input("\nBuscar? → ").strip()
            
            if busqueda.lower() in ['salir', 'exit', 'q']:
                print("\nHasta luego!")
                break
            
            if not busqueda:
                continue
            
            # Cantidad de resultados
            cantidad = preguntar_cantidad()
            
            # Buscar videos
            videos = buscar_videos(busqueda, cantidad)
            
            if not videos:
                print("\nNo hay resultados")
                continue
            
            # Mostrar resultados
            mostrar_videos(videos)
            
            # Reproducir
            while True:
                num = preguntar_video(len(videos))
                
                if num is None:
                    break
                
                # Preguntar calidad
                formato = preguntar_calidad()
                
                # Reproducir con metodo anti-bloqueo
                video = videos[num-1]
                reproducir_video(video['link'], video['titulo'], formato)
                
                # Preguntar si otro
                otro = input("\nOtro video de esta busqueda? (s/n): ").strip().lower()
                if otro not in ['s', 'si', 'y']:
                    break
                    
        except KeyboardInterrupt:
            print("\n\nHasta luego!")
            break
        except Exception as e:
            print(f"\nError inesperado: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nError fatal: {e}")
        limpiar_archivos_temp()
        sys.exit(1)
