#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XONITUBE 2026 - Lanzador Universal
Este script es el ENCARGADO de ejecutar xonitube.py
Detecta automáticamente el sistema y verifica dependencias
Desarrollado por: Darian Alberto Camacho Salas
"""

import subprocess
import sys
import os
import platform
import shutil

# Colores para terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    
    @staticmethod
    def supports_color():
        """Verifica si la terminal soporta colores"""
        if platform.system() == 'Windows':
            try:
                import ctypes
                kernel32 = ctypes.windll.kernel32
                return kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            except:
                return False
        return True

# Desactivar colores si no hay soporte
if not Colors.supports_color():
    for attr in dir(Colors):
        if not attr.startswith('_') and attr != 'supports_color':
            setattr(Colors, attr, '')

def get_system():
    """Detecta el sistema operativo"""
    return platform.system().lower()

def get_linux_distro():
    """Detecta la distribución de Linux específica"""
    if get_system() != 'linux':
        return None
    
    try:
        if os.path.exists('/etc/os-release'):
            with open('/etc/os-release', 'r') as f:
                content = f.read().lower()
                if 'ubuntu' in content:
                    return 'ubuntu'
                elif 'debian' in content:
                    return 'debian'
                elif 'fedora' in content:
                    return 'fedora'
                elif 'centos' in content:
                    return 'centos'
                elif 'arch' in content:
                    return 'arch'
                elif 'manjaro' in content:
                    return 'manjaro'
                elif 'mint' in content:
                    return 'mint'
        return 'linux-generico'
    except:
        return 'linux-generico'

def get_python_command():
    """Obtiene el comando Python correcto"""
    if get_system() == 'windows':
        return ['python']
    else:
        try:
            subprocess.run(['python3', '--version'], capture_output=True, check=True)
            return ['python3']
        except:
            return ['python']

def print_banner():
    """Muestra el banner de XONITUBE"""
    sistema = get_system()
    distro = get_linux_distro()
    
    sistema_texto = {
        'windows': 'WINDOWS',
        'linux': f'LINUX ({distro.upper()})' if distro else 'LINUX',
        'darwin': 'MACOS'
    }.get(sistema, 'DESCONOCIDO')
    
    banner = f"""
{Colors.BLUE}{Colors.BOLD}╔══════════════════════════════════════════════════════════╗
║                     XONITUBE 2026 v5.7                      ║
║              Reproductor de YouTube desde Terminal           ║
║                   Optimizado para 1GB RAM                    ║
║                                                            ║
║               Sistema detectado: {sistema_texto}            ║
║                                                            ║
║               Desarrollado por: Darian Alberto               ║
║                      Camacho Salas                           ║
╚══════════════════════════════════════════════════════════════╝{Colors.END}
    """
    print(banner)

def check_python():
    """Verifica que Python está instalado"""
    try:
        cmd = get_python_command() + ['--version']
        subprocess.run(cmd, capture_output=True, check=True)
        return True
    except:
        return False

def check_command(comando):
    """Verifica si un comando existe en el sistema"""
    return shutil.which(comando) is not None

def check_dependencies():
    """Verifica las dependencias necesarias para xonitube.py"""
    print(f"\n{Colors.BOLD}Verificando dependencias para XONITUBE...{Colors.END}")
    
    # Verificar mpv
    if check_command('mpv'):
        print(f"{Colors.GREEN}  - mpv OK{Colors.END}")
        mpv_ok = True
    else:
        print(f"{Colors.YELLOW}  - mpv (faltante){Colors.END}")
        mpv_ok = False
    
    # Verificar yt-dlp
    if check_command('yt-dlp'):
        print(f"{Colors.GREEN}  - yt-dlp OK{Colors.END}")
        ytdlp_ok = True
    else:
        print(f"{Colors.YELLOW}  - yt-dlp (faltante){Colors.END}")
        ytdlp_ok = False
    
    return mpv_ok, ytdlp_ok

def install_dependencies_linux(distro, mpv_falta, ytdlp_falta):
    """Instala dependencias en Linux"""
    print(f"\n{Colors.BOLD}Instalando dependencias en Linux ({distro})...{Colors.END}")
    
    if distro in ['ubuntu', 'debian', 'mint']:
        cmd_update = ['sudo', 'apt', 'update']
        cmd_install = ['sudo', 'apt', 'install', '-y']
        if mpv_falta:
            cmd_install.append('mpv')
        if ytdlp_falta:
            cmd_install.append('yt-dlp')
    
    elif distro in ['arch', 'manjaro']:
        cmd_update = ['sudo', 'pacman', '-Sy']
        cmd_install = ['sudo', 'pacman', '-S', '--noconfirm']
        if mpv_falta:
            cmd_install.append('mpv')
        if ytdlp_falta:
            cmd_install.append('yt-dlp')
    
    elif distro in ['fedora']:
        cmd_update = ['sudo', 'dnf', 'check-update']
        cmd_install = ['sudo', 'dnf', 'install', '-y']
        if mpv_falta:
            cmd_install.append('mpv')
        if ytdlp_falta:
            cmd_install.append('yt-dlp')
    
    else:
        print(f"{Colors.YELLOW}Distribución no reconocida. Instala manualmente:{Colors.END}")
        if mpv_falta:
            print("  mpv: sudo apt install mpv  (o el comando de tu distro)")
        if ytdlp_falta:
            print("  yt-dlp: sudo apt install yt-dlp  (o pip install yt-dlp)")
        return False
    
    # Ejecutar actualización
    if mpv_falta or ytdlp_falta:
        try:
            print(f"Ejecutando: {' '.join(cmd_update)}")
            subprocess.run(cmd_update, check=False)
            
            print(f"Ejecutando: {' '.join(cmd_install)}")
            subprocess.run(cmd_install, check=True)
            print(f"{Colors.GREEN}Instalación completada{Colors.END}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"{Colors.RED}Error en la instalación: {e}{Colors.END}")
            return False
    
    return True

def install_dependencies_macos(mpv_falta, ytdlp_falta):
    """Instala dependencias en macOS"""
    print(f"\n{Colors.BOLD}Instalando dependencias en macOS...{Colors.END}")
    
    # Verificar si brew está instalado
    if not check_command('brew'):
        print(f"{Colors.YELLOW}Homebrew no está instalado{Colors.END}")
        print("Instala Homebrew desde: https://brew.sh/")
        print("\nO instala manualmente:")
        if mpv_falta:
            print("  mpv: brew install mpv")
        if ytdlp_falta:
            print("  yt-dlp: pip3 install yt-dlp")
        return False
    
    try:
        if mpv_falta:
            print("Instalando mpv...")
            subprocess.run(['brew', 'install', 'mpv'], check=True)
        
        if ytdlp_falta:
            print("Instalando yt-dlp...")
            subprocess.run(['pip3', 'install', 'yt-dlp'], check=True)
        
        print(f"{Colors.GREEN}Instalación completada{Colors.END}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"{Colors.RED}Error en la instalación: {e}{Colors.END}")
        return False

def install_dependencies_windows(mpv_falta, ytdlp_falta):
    """Instala dependencias en Windows"""
    print(f"\n{Colors.BOLD}Instalando dependencias en Windows...{Colors.END}")
    
    instrucciones = []
    
    if mpv_falta:
        instrucciones.append("""
  mpv: Descarga desde https://mpv.io/installation/
  - Descarga el archivo .exe o .7z
  - Extrae en C:\\mpv
  - Agrega C:\\mpv a tu PATH""")
    
    if ytdlp_falta:
        instrucciones.append("""
  yt-dlp: pip install yt-dlp""")
    
    print(f"{Colors.YELLOW}Instrucciones para Windows:{Colors.END}")
    for inst in instrucciones:
        print(inst)
    
    # Intentar instalar yt-dlp con pip
    if ytdlp_falta:
        try:
            print("\nIntentando instalar yt-dlp con pip...")
            subprocess.run([sys.executable, '-m', 'pip', 'install', 'yt-dlp'], check=True)
            print(f"{Colors.GREEN}yt-dlp instalado correctamente{Colors.END}")
        except:
            print(f"{Colors.YELLOW}No se pudo instalar yt-dlp automáticamente{Colors.END}")
    
    return True

def mostrar_instrucciones_python():
    """Muestra instrucciones para instalar Python"""
    sistema = get_system()
    
    if sistema == 'windows':
        print("   Descarga Python desde: https://www.python.org/downloads/")
        print("   IMPORTANTE: Al instalar, marca 'Add Python to PATH'")
    elif sistema == 'linux':
        distro = get_linux_distro()
        if distro in ['ubuntu', 'debian', 'mint']:
            print("   sudo apt update")
            print("   sudo apt install python3 python3-pip")
        elif distro in ['arch', 'manjaro']:
            print("   sudo pacman -S python python-pip")
        else:
            print("   Instala Python 3 desde: https://www.python.org/downloads/")
    elif sistema == 'darwin':
        print("   Instala con: brew install python3")
        print("   O descarga desde: https://www.python.org/downloads/")

def main():
    """Función principal - Ejecuta xonitube.py"""
    # Limpiar pantalla según sistema
    if get_system() == 'windows':
        os.system('cls')
    else:
        os.system('clear')
    
    # Mostrar banner
    print_banner()
    
    sistema = get_system()
    distro = get_linux_distro()
    
    print(f"{Colors.BOLD}Sistema operativo:{Colors.END} {sistema}")
    if distro:
        print(f"{Colors.BOLD}Distribucion:{Colors.END} {distro}")
    
    # Verificar Python
    if not check_python():
        print(f"\n{Colors.RED}Error: Python no esta instalado{Colors.END}")
        mostrar_instrucciones_python()
        input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")
        return
    
    python_version = subprocess.run(get_python_command() + ['--version'], 
                                   capture_output=True, text=True).stdout.strip()
    print(f"{Colors.BOLD}Python:{Colors.END} {python_version}")
    print(f"{Colors.BOLD}Ruta:{Colors.END} {os.path.dirname(os.path.abspath(__file__))}")
    
    # Verificar dependencias
    mpv_falta, ytdlp_falta = check_dependencies()
    
    # Instalar dependencias si faltan
    if mpv_falta or ytdlp_falta:
        print(f"\n{Colors.YELLOW}Faltan dependencias{Colors.END}")
        
        if sistema == 'linux':
            respuesta = input("Instalar automaticamente? (s/n): ")
            if respuesta.lower() == 's':
                install_dependencies_linux(distro, mpv_falta, ytdlp_falta)
            else:
                print(f"\n{Colors.YELLOW}Puedes instalarlas manualmente:{Colors.END}")
                if mpv_falta:
                    print("  sudo apt install mpv  (o el comando de tu distro)")
                if ytdlp_falta:
                    print("  sudo apt install yt-dlp")
        
        elif sistema == 'darwin':
            respuesta = input("Instalar automaticamente? (s/n): ")
            if respuesta.lower() == 's':
                install_dependencies_macos(mpv_falta, ytdlp_falta)
        
        elif sistema == 'windows':
            install_dependencies_windows(mpv_falta, ytdlp_falta)
            input(f"\n{Colors.YELLOW}Presiona Enter para continuar...{Colors.END}")
    
    # Verificar que existe xonitube.py
    if not os.path.exists('xonitube.py'):
        print(f"\n{Colors.RED}Error: No se encuentra xonitube.py{Colors.END}")
        print(f"   Archivos encontrados: {', '.join(os.listdir('.')[:5])}")
        input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")
        return
    
    print(f"\n{Colors.BOLD}Iniciando XONITUBE...{Colors.END}")
    print(f"{Colors.BOLD}Para salir:{Colors.END} Ctrl+C")
    print("-" * 60)
    
    # Ejecutar xonitube.py
    try:
        python_cmd = get_python_command()
        subprocess.run(python_cmd + ['xonitube.py'])
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Programa detenido por el usuario{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}Error ejecutando xonitube.py: {e}{Colors.END}")
    
    print(f"\n{Colors.BLUE}Gracias por usar XONITUBE 2026{Colors.END}")
    print(f"{Colors.BLUE}Desarrollado por Darian Alberto Camacho Salas{Colors.END}")
    
    if sistema != 'windows':
        input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")

def crear_accesos_directos():
    """Crea accesos directos según el sistema"""
    sistema = get_system()
    
    if sistema == 'windows':
        # Crear .bat para Windows
        with open('INICIAR_XONITUBE.bat', 'w') as f:
            f.write("""@echo off
title XONITUBE 2026
color 1F
echo ========================================
echo      XONITUBE 2026 - Reproductor YouTube
echo      Desarrollado por Darian Alberto
echo      Optimizado para 1GB RAM
echo ========================================
echo.
python start.py
pause
""")
        print(f"{Colors.GREEN}Creado INICIAR_XONITUBE.bat - Haz doble clic para ejecutar{Colors.END}")
    
    elif sistema == 'linux':
        # Crear .sh para Linux
        with open('INICIAR_XONITUBE.sh', 'w') as f:
            f.write("""#!/bin/bash
echo "========================================"
echo "      XONITUBE 2026 - Reproductor YouTube"
echo "      Desarrollado por Darian Alberto"
echo "      Optimizado para 1GB RAM"
echo "========================================"
echo ""
python3 start.py
read -p "Presiona Enter para salir"
""")
        os.chmod('INICIAR_XONITUBE.sh', 0o755)
        print(f"{Colors.GREEN}Creado INICIAR_XONITUBE.sh - Ejecuta con: ./INICIAR_XONITUBE.sh{Colors.END}")
    
    elif sistema == 'darwin':
        # Crear .command para Mac
        with open('INICIAR_XONITUBE.command', 'w') as f:
            f.write("""#!/bin/bash
cd "$(dirname "$0")"
echo "========================================"
echo "      XONITUBE 2026 - Reproductor YouTube"
echo "      Desarrollado por Darian Alberto"
echo "      Optimizado para 1GB RAM"
echo "========================================"
echo ""
python3 start.py
""")
        os.chmod('INICIAR_XONITUBE.command', 0o755)
        print(f"{Colors.GREEN}Creado INICIAR_XONITUBE.command - Haz doble clic para ejecutar{Colors.END}")

if __name__ == '__main__':
    try:
        # Crear accesos directos
        crear_accesos_directos()
        
        # Ejecutar programa principal
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Saliendo...{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}Error inesperado: {e}{Colors.END}")
        input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")
