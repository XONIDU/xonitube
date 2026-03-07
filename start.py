#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XoniTube v5.0 - Buscador ultra optimizado
Creado por Darian Alberto Camacho Salas
Consumo minimo de recursos - Ideal para 1GB RAM
"""

import subprocess
import sys
import os
import json
import re
from threading import Thread
from queue import Queue

# ============================================================================
# CONFIGURACION OPTIMIZADA
# ============================================================================

REPRODUCTOR = "mpv"
CACHE_DIR = "/tmp/xonitube_cache"
os.makedirs(CACHE_DIR, exist_ok=True)

# ============================================================================
# FUNCIONES ULTRA RAPIDAS
# ============================================================================

def limpiar_pantalla():
    """Limpia la pantalla"""
    os.system('clear' if os.name == 'posix' else 'cls')

def buscar_videos_rapido(termino, cantidad):
    """
    Busqueda ultra optimizada - usa el metodo mas rapido posible
    """
    print(f"\nBuscando: '{termino}'...")
    
    try:
        # Usar formato mas simple y rapido
        cmd = [
            "yt-dlp",
            "--no-warnings",
            "--quiet",  # Suprimir output innecesario
            "--no-playlist",
            "--flat-playlist",  # Mas rapido, no extrae metadata
            "--print", "%(title)s|%(id)s",
            f"ytsearch{cantidad}:{termino}",
            "--sleep-interval", "0",
            "--force-ipv4",
            "--buffer-size", "16K",  # Buffer pequeno para ahorrar RAM
            "--http-chunk-size", "1M"
        ]
        
        # Ejecutar con timeout corto
        resultado = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            timeout=10,
            preexec_fn=os.setsid  # Para poder matar el proceso facilmente
        )
        
        if resultado.returncode != 0:
            return None
        
        videos = []
        for linea in resultado.stdout.strip().split('\n'):
            if '|' in linea:
                titulo, vid = linea.split('|', 1)
                videos.append({
                    'num': len(videos) + 1,
                    'tit': titulo.strip()[:60],  # Limitar titulo
                    'url': f"https://youtu.be/{vid.strip()}"  # URL corta
                })
        
        return videos if videos else None
        
    except subprocess.TimeoutExpired:
        print("  Tiempo excedido")
        return None
    except Exception as e:
        return None

def mostrar_resultados(videos):
    """Muestra resultados en formato compacto"""
    print("\n" + "-"*50)
    for v in videos:
        print(f"{v['num']}. {v['tit']}")
    print("-"*50)

def reproducir_optimizado(url, calidad):
    """
    Reproduccion con minimo consumo de recursos
    """
    print(f"\n▶ Cargando...")
    
    try:
        # Usar opciones de minimo consumo
        cmd_yt = [
            "yt-dlp",
            "-f", calidad,
            "-o", "-",
            "--no-part",
            "--no-mtime",
            "--quiet",
            "--no-warnings",
            "--buffer-size", "16K",
            "--http-chunk-size", "1M",
            "--throttled-rate", "100K",  # Limitar velocidad si es necesario
            url
        ]
        
        cmd_mpv = [
            REPRODUCTOR,
            "--cache=yes",
            "--cache-secs=10",  # Cache reducido
            "--demuxer-max-bytes=50M",  # Reducido
            "--demuxer-readahead-secs=5",  # Reducido
            "--vd-lavc-fast",  # Decodificacion rapida
            "--vd-lavc-skip-loop-filter=all",  # Saltar filtros pesados
            "--profile=fast",  # Perfil rapido
            "--no-input-default-bindings",
            "--really-quiet",
            "-"
        ]
        
        # Ejecutar con prioridad baja para no saturar el sistema
        p1 = subprocess.Popen(
            cmd_yt, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
            preexec_fn=os.setsid
        )
        
        p2 = subprocess.Popen(
            cmd_mpv, 
            stdin=p1.stdout,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            preexec_fn=os.setsid
        )
        
        p2.wait()
        
        # Limpiar
        try:
            os.killpg(os.getpgid(p1.pid), 15)
        except:
            pass
            
        return True
        
    except:
        return False

def preguntar_cantidad():
    """Pregunta rapida"""
    try:
        cant = input("\nCuantos? (1-5, Enter=3): ").strip()
        if cant == "":
            return 3
        cant = int(cant)
        if 1 <= cant <= 5:
            return cant
        return 3
    except:
        return 3

def preguntar_calidad_rapida():
    """Seleccion rapida de calidad"""
    print("\nCalidad: 1=P 2=144 3=240 4=360 5=A")
    op = input("→ ").strip()
    
    calidades = {
        '1': "worst",
        '2': "worst[height<=144]",
        '3': "worst[height<=240]",
        '4': "worst[height<=360]",
        '5': "bestaudio"
    }
    return calidades.get(op, "worst")

# ============================================================================
# PROGRAMA PRINCIPAL OPTIMIZADO
# ============================================================================

def main():
    """Funcion principal con minimo consumo"""
    
    limpiar_pantalla()
    print("="*50)
    print("XONITUBE v5.0".center(50))
    print("="*50)
    print("Creado por Darian Alberto Camacho Salas".center(50))
    print("="*50)
    print("\nModo ultra optimizado - 1GB RAM")
    print("Comandos: buscar, salir")
    
    while True:
        try:
            # Entrada simple
            entrada = input("\n> ").strip()
            
            if entrada.lower() in ['salir', 'q', 'exit']:
                break
            
            if not entrada:
                continue
            
            # Si empieza con 'b ' es busqueda
            if entrada.startswith('b '):
                termino = entrada[2:]
                cantidad = preguntar_cantidad()
                
                # Buscar
                videos = buscar_videos_rapido(termino, cantidad)
                
                if not videos:
                    print("Sin resultados")
                    continue
                
                # Mostrar
                mostrar_resultados(videos)
                
                # Seleccionar
                try:
                    sel = input("\nNum? (Enter=menu): ").strip()
                    if sel and sel.isdigit():
                        idx = int(sel) - 1
                        if 0 <= idx < len(videos):
                            calidad = preguntar_calidad_rapida()
                            reproducir_optimizado(videos[idx]['url'], calidad)
                except:
                    pass
            
            # Busqueda directa (asume que es busqueda)
            else:
                cantidad = preguntar_cantidad()
                videos = buscar_videos_rapido(entrada, cantidad)
                
                if not videos:
                    print("Sin resultados")
                    continue
                
                mostrar_resultados(videos)
                
                try:
                    sel = input("\nNum? (Enter=menu): ").strip()
                    if sel and sel.isdigit():
                        idx = int(sel) - 1
                        if 0 <= idx < len(videos):
                            calidad = preguntar_calidad_rapida()
                            reproducir_optimizado(videos[idx]['url'], calidad)
                except:
                    pass
                    
        except KeyboardInterrupt:
            print("\n\nAdios!")
            break
        except:
            continue

if __name__ == "__main__":
    try:
        main()
    except:
        pass
    finally:
        # Limpiar cache
        try:
            os.system(f"rm -rf {CACHE_DIR}/* 2>/dev/null")
        except:
            pass
