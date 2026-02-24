#XoniTube v1.0 - Buscador conversacional de YouTube para terminal
#Creado por Darian Alberto Camacho Salas

import subprocess
import sys
import os
from youtubesearchpython import VideosSearch

# ============================================================================
# CONFIGURACION
# ============================================================================

MAX_RESULTADOS = 10
CALIDAD_VIDEO = "worst"
REPRODUCTOR = "mpv"

# ============================================================================
# FUNCIONES
# ============================================================================

def limpiar_pantalla():
    """Limpia la pantalla de la terminal"""
    os.system('clear' if os.name == 'posix' else 'cls')

def buscar_videos(termino):
    """
    Busca videos en YouTube
    """
    try:
        print(f"\nBuscando: '{termino}'...\n")
        busqueda = VideosSearch(termino, limit=MAX_RESULTADOS)
        resultados = busqueda.result()['result']
        
        videos = []
        for video in resultados:
            videos.append({
                'titulo': video['title'],
                'duracion': video.get('duration', 'N/A'),
                'link': video['link'],
                'canal': video['channel']['name']
            })
        return videos
    except Exception as e:
        print(f"Error en la busqueda: {e}")
        return None

def mostrar_videos(videos):
    """Muestra la lista de videos numerada"""
    print("\n" + "="*60)
    print("RESULTADOS".center(60))
    print("="*60)
    
    for i, video in enumerate(videos, 1):
        print(f"\n{i}. {video['titulo']}")
        print(f"   Duracion: {video['duracion']} | Canal: {video['canal']}")
    print("\n" + "="*60)

def reproducir_video(link, numero, titulo):
    """Reproduce un video"""
    print(f"\nReproduciendo video #{numero}: {titulo[:50]}...")
    print(f"Calidad: {CALIDAD_VIDEO}")
    print(f"Presiona Ctrl+C para volver al menu\n")
    
    try:
        cmd = [REPRODUCTOR, "--ytdl-format=" + CALIDAD_VIDEO, link]
        subprocess.run(cmd)
        return True
    except KeyboardInterrupt:
        print("\n\nReproduccion detenida")
        return True
    except Exception as e:
        print(f"Error al reproducir: {e}")
        return False

def mostrar_ayuda():
    """Muestra la ayuda"""
    print("\n" + "="*60)
    print("AYUDA DE XONITUBE".center(60))
    print("="*60)
    print("""
COMANDOS DISPONIBLES:
  buscar <termino>  - Busca videos
  listar            - Muestra la ultima busqueda
  reproducir <num>  - Reproduce un video por su numero
  calidad <opcion>  - Cambia calidad (worst/144p/240p/360p)
  ayuda             - Muestra esta ayuda
  salir             - Termina el programa

EJEMPLOS:
  > buscar gatos graciosos
  > reproducir 3
  > calidad 144p
    """)
    print("="*60)

# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

def main():
    """Funcion principal"""
    
    ultima_busqueda = []
    calidad_actual = CALIDAD_VIDEO
    
    # Mensaje de bienvenida
    limpiar_pantalla()
    print("="*60)
    print("XONITUBE v1.0".center(60))
    print("="*60)
    print("Creado por Darian Alberto Camacho Salas".center(60))
    print("="*60)
    print("\nEscribe 'ayuda' para ver los comandos disponibles")
    
    while True:
        try:
            # Input principal
            comando = input("\nXoniTube> ").strip().lower()
            
            if not comando:
                continue
            
            # Procesar comandos
            if comando in ["salir", "exit"]:
                print("\nHasta luego! Gracias por usar XoniTube")
                break
            
            elif comando in ["ayuda", "help"]:
                mostrar_ayuda()
            
            elif comando in ["listar", "lista"]:
                if ultima_busqueda:
                    mostrar_videos(ultima_busqueda)
                else:
                    print("No hay ninguna busqueda reciente")
            
            elif comando.startswith("calidad "):
                partes = comando.split(" ", 1)
                if len(partes) > 1:
                    nueva_calidad = partes[1]
                    calidad_actual = nueva_calidad
                    print(f"Calidad cambiada a: {calidad_actual}")
                else:
                    print("Uso: calidad <opcion>")
            
            elif comando.startswith("buscar "):
                partes = comando.split(" ", 1)
                if len(partes) > 1:
                    termino = partes[1]
                    videos = buscar_videos(termino)
                    
                    if videos:
                        ultima_busqueda = videos
                        mostrar_videos(videos)
                        print("\nUsa 'reproducir <numero>' para ver un video")
                else:
                    print("Uso: buscar <termino>")
            
            elif comando.startswith("reproducir "):
                partes = comando.split(" ", 1)
                if len(partes) > 1:
                    if not ultima_busqueda:
                        print("Primero debes hacer una busqueda")
                        continue
                    
                    try:
                        num = int(partes[1])
                        if 1 <= num <= len(ultima_busqueda):
                            video = ultima_busqueda[num-1]
                            reproducir_video(video['link'], num, video['titulo'])
                        else:
                            print(f"Numero invalido. Debe ser entre 1 y {len(ultima_busqueda)}")
                    except ValueError:
                        print("Debes especificar un numero valido")
                else:
                    print("Uso: reproducir <numero>")
            
            elif comando in ["cls", "clear"]:
                limpiar_pantalla()
            
            else:
                print(f"Comando no reconocido: '{comando}'")
                print("Escribe 'ayuda' para ver los comandos disponibles")
        
        except KeyboardInterrupt:
            print("\n\nHasta luego!")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")

# ============================================================================
# PUNTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nError fatal: {e}")
        sys.exit(1)
