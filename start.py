#XoniTube v1.0 - Buscador interactivo de YouTube para terminal
#Creado por Darian Alberto Camacho Salas

import curses
import subprocess
import sys
import time
from youtubesearchpython import VideosSearch

# ============================================================================
# CONFIGURACION
# ============================================================================

MAX_RESULTADOS = 15  # Numero de resultados por busqueda
CALIDAD_VIDEO = "worst"  # worst, worstvideo, 144p, 240p, etc.
REPRODUCTOR = "mpv"  # mpv o mplayer

# ============================================================================
# FUNCIONES DE BUSQUEDA Y REPRODUCCION
# ============================================================================

def buscar_videos(termino):
    """
    Busca videos en YouTube usando youtube-search-python
    Retorna una lista de diccionarios con titulo, duracion y link
    """
    try:
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
        return f"Error en la busqueda: {e}"

def reproducir_video(link):
    """
    Reproduce un video con mpv en la calidad mas baja
    """
    try:
        # Comando para mpv con la calidad minima
        cmd = [REPRODUCTOR, "--ytdl-format=" + CALIDAD_VIDEO, link]
        subprocess.run(cmd)
        return True
    except Exception as e:
        return False

# ============================================================================
# INTERFAZ DE TERMINAL CON CURSES
# ============================================================================

def mostrar_bienvenida(stdscr):
    """Pantalla de bienvenida inicial con creditos"""
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    
    # Titulo principal
    titulo = "XONITUBE v1.0"
    x_titulo = width // 2 - len(titulo) // 2
    y_titulo = height // 3
    
    stdscr.attron(curses.A_BOLD)
    stdscr.addstr(y_titulo, x_titulo, titulo)
    stdscr.attroff(curses.A_BOLD)
    
    # Creditos
    creditos = "Creado por Darian Alberto Camacho Salas"
    x_cred = width // 2 - len(creditos) // 2
    stdscr.addstr(y_titulo + 2, x_cred, creditos)
    
    # Subtitulo
    subtitulo = "Buscador de YouTube para PC"
    x_sub = width // 2 - len(subtitulo) // 2
    stdscr.addstr(y_titulo + 4, x_sub, subtitulo)
    
    # Mensaje de continuar
    continuar = "Presiona cualquier tecla para continuar..."
    x_cont = width // 2 - len(continuar) // 2
    stdscr.addstr(y_titulo + 6, x_cont, continuar)
    
    stdscr.refresh()
    stdscr.getch()

def buscar_interactivo(stdscr):
    """Pantalla de busqueda"""
    stdscr.clear()
    curses.echo()  # Mostrar lo que el usuario escribe
    height, width = stdscr.getmaxyx()
    
    # Pregunta
    pregunta = "Que quieres buscar? (o 'salir' para terminar): "
    stdscr.addstr(1, 2, pregunta)
    
    # Campo de entrada
    curses.textpad.rectangle(stdscr, 2, 2, 4, width - 4)
    curses.curs_set(1)  # Mostrar cursor
    
    # Obtener entrada del usuario
    respuesta = stdscr.getstr(3, 4, width - 10).decode('utf-8')
    
    curses.noecho()
    curses.curs_set(0)
    return respuesta.strip()

def mostrar_lista_videos(stdscr, videos, seleccion=0, mensaje=""):
    """Muestra la lista de videos y permite navegar"""
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    
    # Titulo
    stdscr.attron(curses.A_BOLD)
    stdscr.addstr(0, 2, "RESULTADOS DE BUSQUEDA")
    stdscr.attroff(curses.A_BOLD)
    
    # Instrucciones
    instrucciones = "[Flechas Arriba/Abajo] Navegar | [Enter] Reproducir | [B] Buscar de nuevo | [Q] Salir"
    stdscr.addstr(height - 2, 2, instrucciones[:width-5])
    
    # Mostrar mensaje si existe
    if mensaje:
        stdscr.attron(curses.A_REVERSE)
        stdscr.addstr(height - 4, 2, mensaje[:width - 5])
        stdscr.attroff(curses.A_REVERSE)
    
    # Calcular area para la lista
    inicio_y = 2
    fin_y = height - 4
    max_visibles = fin_y - inicio_y - 1
    
    # Si no hay videos
    if not videos:
        stdscr.addstr(inicio_y, 2, "No se encontraron videos")
        stdscr.refresh()
        stdscr.getch()
        return None, "no_videos"
    
    # Mostrar lista con scroll si es necesario
    inicio_lista = max(0, seleccion - max_visibles // 2)
    fin_lista = min(len(videos), inicio_lista + max_visibles)
    
    for i in range(inicio_lista, fin_lista):
        y = inicio_y + i - inicio_lista
        video = videos[i]
        
        # Preparar el texto del video
        titulo = video['titulo']
        duracion = video['duracion']
        canal = video['canal']
        
        # Limitar longitudes
        if len(titulo) > width - 30:
            titulo = titulo[:width - 33] + "..."
        
        # Formato: Numero. Titulo (duracion) - Canal
        texto = f"{i+1}. {titulo} ({duracion}) - {canal}"
        
        # Resaltar la seleccion actual
        if i == seleccion:
            stdscr.attron(curses.A_REVERSE)
        
        # Escribir el video en pantalla
        try:
            stdscr.addstr(y, 2, texto[:width - 5])
        except curses.error:
            # Ignorar errores de escritura (ultima linea, etc.)
            pass
        
        if i == seleccion:
            stdscr.attroff(curses.A_REVERSE)
    
    # Mostrar contador de paginas
    contador = f"Mostrando {inicio_lista + 1}-{fin_lista} de {len(videos)}"
    stdscr.addstr(fin_y - 1, 2, contador)
    
    stdscr.refresh()
    return seleccion, None

def pantalla_reproduciendo(stdscr, video):
    """Pantalla mientras se reproduce el video"""
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    
    stdscr.attron(curses.A_BOLD)
    stdscr.addstr(height // 3, width // 2 - 13, "REPRODUCIENDO VIDEO")
    stdscr.attroff(curses.A_BOLD)
    
    # Mostrar titulo del video (limitado)
    titulo = video['titulo']
    if len(titulo) > width - 10:
        titulo = titulo[:width - 13] + "..."
    
    stdscr.addstr(height // 3 + 2, width // 2 - len(titulo) // 2, titulo)
    stdscr.addstr(height // 3 + 4, width // 2 - 12, "Cargando... por favor espera")
    
    stdscr.refresh()
    
    # Iniciar reproduccion
    exito = reproducir_video(video['link'])
    
    if not exito:
        stdscr.addstr(height // 3 + 6, width // 2 - 11, "Error al reproducir")
        stdscr.refresh()
        time.sleep(2)
    
    return exito

def confirmar_salida(stdscr):
    """Pregunta si realmente quiere salir"""
    height, width = stdscr.getmaxyx()
    
    stdscr.attron(curses.A_REVERSE)
    stdscr.addstr(height // 2 - 2, width // 2 - 20, " " * 40)
    stdscr.addstr(height // 2 - 1, width // 2 - 20, " Estas seguro de que quieres salir? (S/N) ")
    stdscr.addstr(height // 2, width // 2 - 20, " " * 40)
    stdscr.attroff(curses.A_REVERSE)
    
    stdscr.refresh()
    
    while True:
        tecla = stdscr.getch()
        if tecla in [ord('s'), ord('S')]:
            return True
        elif tecla in [ord('n'), ord('N'), 27]:  # 27 es ESC
            return False

# ============================================================================
# FUNCION PRINCIPAL
# ============================================================================

def main(stdscr):
    """Funcion principal que maneja toda la logica del programa"""
    
    # Configuracion inicial de curses
    curses.curs_set(0)  # Ocultar cursor
    curses.start_color()
    curses.use_default_colors()
    
    # Variables de estado
    videos = []
    seleccion = 0
    ultima_busqueda = ""
    
    # Pantalla de bienvenida
    mostrar_bienvenida(stdscr)
    
    while True:
        # PASO 1: BUSCAR
        termino = buscar_interactivo(stdscr)
        
        if termino.lower() == 'salir':
            if confirmar_salida(stdscr):
                break
            else:
                continue
        
        if not termino:
            continue
        
        ultima_busqueda = termino
        
        # Mostrar mensaje de "Buscando..."
        stdscr.clear()
        stdscr.addstr(5, 5, f"Buscando: '{termino}'...")
        stdscr.refresh()
        
        # Realizar busqueda
        resultado = buscar_videos(termino)
        
        if isinstance(resultado, str):
            # Error
            stdscr.clear()
            stdscr.addstr(5, 5, resultado)
            stdscr.addstr(7, 5, "Presiona cualquier tecla para continuar...")
            stdscr.refresh()
            stdscr.getch()
            continue
        else:
            videos = resultado
            seleccion = 0
        
        # PASO 2: MOSTRAR LISTA Y NAVEGAR
        while True:
            # Mostrar lista
            seleccion, error = mostrar_lista_videos(stdscr, videos, seleccion)
            
            if error == "no_videos":
                break
            
            # Manejar teclas
            tecla = stdscr.getch()
            
            if tecla == ord('q') or tecla == ord('Q'):
                if confirmar_salida(stdscr):
                    return
                else:
                    continue
            
            elif tecla == ord('b') or tecla == ord('B'):
                # Volver a buscar
                break
            
            elif tecla == curses.KEY_UP:
                seleccion = max(0, seleccion - 1)
            
            elif tecla == curses.KEY_DOWN:
                seleccion = min(len(videos) - 1, seleccion + 1)
            
            elif tecla == 10:  # Enter
                # Reproducir video seleccionado
                video_seleccionado = videos[seleccion]
                pantalla_reproduciendo(stdscr, video_seleccionado)
                # Al volver de la reproduccion, mostrar mensaje
                mensaje = f"Reproducido: {video_seleccionado['titulo'][:40]}..."
                mostrar_lista_videos(stdscr, videos, seleccion, mensaje)
                stdscr.getch()  # Esperar tecla para continuar

# ============================================================================
# PUNTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    # Verificar dependencias
    try:
        import curses
        from youtubesearchpython import VideosSearch
    except ImportError as e:
        print(f"Error: Falta una dependencia - {e}")
        print("\nPara instalar lo necesario:")
        print("  pip3 install youtube-search-python windows-curses")
        print("  sudo apt install mpv")
        sys.exit(1)
    
    # Verificar reproductor
    try:
        subprocess.run([REPRODUCTOR, "--version"], 
                      stdout=subprocess.DEVNULL, 
                      stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        print(f"Error: No se encuentra {REPRODUCTOR}")
        print(f"  Instalalo con: sudo apt install {REPRODUCTOR}")
        sys.exit(1)
    
    # Iniciar aplicacion
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        print("\n\nHasta luego! Gracias por usar XoniTube")
    except Exception as e:
        print(f"\nError inesperado: {e}")
        sys.exit(1)
    
    # Mensaje de despedida
    print("\nXoniTube finalizado. Creado por Darian Alberto Camacho Salas - Vuelve pronto!")
