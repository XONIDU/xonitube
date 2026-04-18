#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XONITUBE 2026 - Lanzador Universal (Robusto)
Reproductor de YouTube desde terminal para 1GB RAM
Incluye instalación automática de pip, yt-dlp y mpv
Desarrollado por: Darian Alberto Camacho Salas
Organización: XONIDU
"""

import subprocess
import sys
import os
import platform
import shutil
import time

# ============================================================================
# Colores para terminal
# ============================================================================
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    END = '\033[0m'
    BOLD = '\033[1m'
    
    @staticmethod
    def supports_color():
        if platform.system() == 'Windows':
            try:
                import ctypes
                kernel32 = ctypes.windll.kernel32
                return kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            except:
                return False
        return True

if not Colors.supports_color():
    for attr in dir(Colors):
        if not attr.startswith('_') and attr != 'supports_color':
            setattr(Colors, attr, '')

# ============================================================================
# Detección del sistema
# ============================================================================
def get_system():
    return platform.system().lower()

def get_linux_distro():
    if get_system() != 'linux':
        return None
    try:
        if os.path.exists('/etc/os-release'):
            with open('/etc/os-release', 'r') as f:
                content = f.read().lower()
                if 'ubuntu' in content or 'debian' in content or 'mint' in content or 'antix' in content:
                    return 'debian-based'
                elif 'arch' in content or 'manjaro' in content:
                    return 'arch-based'
                elif 'fedora' in content:
                    return 'fedora'
                elif 'centos' in content or 'rhel' in content:
                    return 'centos'
                elif 'opensuse' in content:
                    return 'opensuse'
        if shutil.which('apt'):
            return 'debian-based'
        elif shutil.which('pacman'):
            return 'arch-based'
        elif shutil.which('dnf'):
            return 'fedora'
        elif shutil.which('yum'):
            return 'centos'
        elif shutil.which('zypper'):
            return 'opensuse'
        return 'linux-generico'
    except:
        return 'linux-generico'

def get_python_command():
    if get_system() == 'windows':
        return ['python']
    else:
        try:
            subprocess.run(['python3', '--version'], capture_output=True, check=True)
            return ['python3']
        except:
            return ['python']

def get_pip_command():
    return [sys.executable, '-m', 'pip']

def get_install_flags():
    flags = []
    sistema = get_system()
    distro = get_linux_distro()
    if sistema == 'linux':
        if distro in ['arch-based', 'fedora']:
            flags.append('--break-system-packages')
        else:
            flags.append('--user')
    elif sistema == 'darwin':
        flags.append('--user')
    return flags

def print_banner():
    sistema = get_system()
    distro = get_linux_distro()
    sistema_texto = {
        'windows': 'WINDOWS',
        'linux': f'LINUX ({distro.upper()})' if distro else 'LINUX',
        'darwin': 'MACOS'
    }.get(sistema, 'DESCONOCIDO')
    
    banner = f"""
{Colors.PURPLE}{Colors.BOLD}╔══════════════════════════════════════════════════════════╗
║                     XONITUBE 2026 v5.9                      ║
║              Reproductor de YouTube desde Terminal           ║
║                   Optimizado para 1GB RAM                    ║
║                                                            ║
║               Sistema detectado: {sistema_texto:<27} ║
║                                                            ║
║               Desarrollado por: Darian Alberto             ║
║                      Camacho Salas                         ║
║                      Organización: XONIDU                  ║
╚══════════════════════════════════════════════════════════════╝{Colors.END}
    """
    print(banner)

# ============================================================================
# Verificación e instalación de pip
# ============================================================================
def check_python():
    try:
        cmd = get_python_command() + ['--version']
        subprocess.run(cmd, capture_output=True, check=True)
        return True
    except:
        return False

def check_pip():
    try:
        cmd = get_pip_command() + ['--version']
        subprocess.run(cmd, capture_output=True, check=True)
        return True
    except:
        return False

def install_pip_linux():
    distro = get_linux_distro()
    print(f"{Colors.YELLOW}Instalando pip en Linux ({distro})...{Colors.END}")
    if distro == 'debian-based':
        try:
            subprocess.run(['sudo', 'apt', 'update'], check=False)
            subprocess.run(['sudo', 'apt', 'install', '-y', 'python3-pip'], check=True)
            return True
        except:
            return False
    elif distro == 'arch-based':
        try:
            subprocess.run(['sudo', 'pacman', '-S', '--noconfirm', 'python-pip'], check=True)
            return True
        except:
            return False
    elif distro == 'fedora':
        try:
            subprocess.run(['sudo', 'dnf', 'install', '-y', 'python3-pip'], check=True)
            return True
        except:
            return False
    elif distro == 'centos':
        try:
            subprocess.run(['sudo', 'yum', 'install', '-y', 'python3-pip'], check=True)
            return True
        except:
            return False
    elif distro == 'opensuse':
        try:
            subprocess.run(['sudo', 'zypper', 'install', '-y', 'python3-pip'], check=True)
            return True
        except:
            return False
    return False

def install_pip_windows():
    print(f"{Colors.YELLOW}Instalando pip en Windows...{Colors.END}")
    try:
        subprocess.run([sys.executable, '-m', 'ensurepip', '--upgrade'], check=True)
        return True
    except:
        try:
            import urllib.request
            urllib.request.urlretrieve('https://bootstrap.pypa.io/get-pip.py', 'get-pip.py')
            subprocess.run([sys.executable, 'get-pip.py'], check=True)
            os.remove('get-pip.py')
            return True
        except:
            return False

# ============================================================================
# Instalación de dependencias del sistema (mpv, yt-dlp)
# ============================================================================
def check_mpv():
    return shutil.which('mpv') is not None

def check_ytdlp():
    return shutil.which('yt-dlp') is not None

def install_mpv_linux():
    distro = get_linux_distro()
    print(f"{Colors.YELLOW}Instalando mpv en {distro}...{Colors.END}")
    try:
        if distro == 'debian-based':
            subprocess.run(['sudo', 'apt', 'update'], check=False)
            subprocess.run(['sudo', 'apt', 'install', '-y', 'mpv'], check=True)
        elif distro == 'arch-based':
            subprocess.run(['sudo', 'pacman', '-S', '--noconfirm', 'mpv'], check=True)
        elif distro == 'fedora':
            subprocess.run(['sudo', 'dnf', 'install', '-y', 'mpv'], check=True)
        elif distro == 'centos':
            subprocess.run(['sudo', 'yum', 'install', '-y', 'mpv'], check=True)
        elif distro == 'opensuse':
            subprocess.run(['sudo', 'zypper', 'install', '-y', 'mpv'], check=True)
        else:
            return False
        return True
    except:
        return False

def install_mpv_macos():
    if not shutil.which('brew'):
        print(f"{Colors.RED}Homebrew no instalado. Instala mpv manualmente: brew install mpv{Colors.END}")
        return False
    try:
        subprocess.run(['brew', 'install', 'mpv'], check=True)
        return True
    except:
        return False

def install_mpv_windows():
    print(f"{Colors.YELLOW}mpv no encontrado. Instrucciones para Windows:{Colors.END}")
    print("  1. Descarga mpv desde: https://mpv.io/installation/")
    print("  2. Extrae el archivo .7z en C:\\mpv")
    print("  3. Agrega C:\\mpv a tu PATH del sistema")
    print("  4. Reinicia la terminal")
    return False

def install_ytdlp():
    """
    Instala o actualiza yt-dlp usando el gestor nativo si es posible (pacman, apt, etc.),
    y si no, mediante pip con los flags adecuados.
    En Arch-based se fuerza el uso de pacman.
    """
    sistema = get_system()
    distro = get_linux_distro()
    
    if sistema == 'linux' and distro == 'arch-based':
        # En Arch, instalar con pacman (mejor que pip)
        print(f"{Colors.YELLOW}Instalando yt-dlp desde pacman (Arch)...{Colors.END}")
        try:
            subprocess.run(['sudo', 'pacman', '-S', '--noconfirm', 'yt-dlp'], check=True)
            print(f"{Colors.GREEN}yt-dlp instalado correctamente desde pacman.{Colors.END}")
            return True
        except Exception as e:
            print(f"{Colors.RED}Fallo instalación con pacman: {e}{Colors.END}")
            print(f"{Colors.YELLOW}Intentando con pip...{Colors.END}")
    
    # Para otros Linux (Debian, Fedora, etc.) usar pip o gestor si existe
    if sistema == 'linux' and distro == 'debian-based':
        # Primero intentar con apt
        try:
            subprocess.run(['sudo', 'apt', 'install', '-y', 'yt-dlp'], check=True)
            print(f"{Colors.GREEN}yt-dlp instalado desde apt.{Colors.END}")
            return True
        except:
            pass
    
    # Si no se instaló con gestor nativo, usar pip
    print(f"{Colors.YELLOW}Instalando/actualizando yt-dlp con pip...{Colors.END}")
    if not check_pip():
        print(f"{Colors.RED}No se encontró pip. Instálalo primero.{Colors.END}")
        return False
    
    flags = get_install_flags()
    # Para evitar errores con --break-system-packages, se puede forzar en Arch aunque usemos pacman
    try:
        cmd = get_pip_command() + ['install', '--upgrade', 'yt-dlp'] + flags
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"{Colors.GREEN}yt-dlp instalado/actualizado con pip.{Colors.END}")
        return True
    except:
        # Intentar sin flags
        try:
            cmd = get_pip_command() + ['install', '--upgrade', 'yt-dlp']
            subprocess.run(cmd, check=True)
            print(f"{Colors.GREEN}yt-dlp instalado/actualizado sin flags.{Colors.END}")
            return True
        except Exception as e:
            print(f"{Colors.RED}Error instalando yt-dlp: {e}{Colors.END}")
            return False

# ============================================================================
# Verificación de xonitube.py y ejecución
# ============================================================================
def check_xonitube():
    return os.path.exists('xonitube.py')

def main():
    # Limpiar pantalla
    if get_system() == 'windows':
        os.system('cls')
    else:
        os.system('clear')
    
    print_banner()
    
    sistema = get_system()
    distro = get_linux_distro()
    print(f"{Colors.BOLD}Sistema operativo:{Colors.END} {sistema}")
    if distro:
        print(f"{Colors.BOLD}Distribución:{Colors.END} {distro}")
    print(f"{Colors.BOLD}Directorio:{Colors.END} {os.getcwd()}")
    
    # Verificar Python
    if not check_python():
        print(f"\n{Colors.RED}❌ Python no está instalado o no está en el PATH.{Colors.END}")
        sys.exit(1)
    
    # Mostrar versión de Python
    ver_py = subprocess.run(get_python_command() + ['--version'], capture_output=True, text=True).stdout.strip()
    print(f"{Colors.BOLD}Python:{Colors.END} {ver_py}")
    
    # Verificar pip e instalarlo si falta
    if not check_pip():
        print(f"\n{Colors.YELLOW}⚠️ Pip no encontrado. Instalando...{Colors.END}")
        if sistema == 'linux':
            if not install_pip_linux():
                print(f"{Colors.RED}No se pudo instalar pip. Instálalo manualmente.{Colors.END}")
                sys.exit(1)
        elif sistema == 'windows':
            if not install_pip_windows():
                print(f"{Colors.RED}No se pudo instalar pip. Ejecuta como administrador.{Colors.END}")
                sys.exit(1)
        else:
            print(f"{Colors.YELLOW}Instala pip manualmente con: python -m ensurepip --upgrade{Colors.END}")
            sys.exit(1)
    else:
        print(f"{Colors.GREEN}✓ Pip disponible{Colors.END}")
    
    # Verificar e instalar/actualizar yt-dlp (robusto)
    if not check_ytdlp():
        print(f"\n{Colors.YELLOW}⚠️ yt-dlp no encontrado. Instalando...{Colors.END}")
        if not install_ytdlp():
            print(f"{Colors.RED}Fallo crítico: no se pudo instalar yt-dlp. Abortando.{Colors.END}")
            sys.exit(1)
    else:
        # Incluso si existe, intentamos actualizar (opcional, pero recomendado)
        print(f"\n{Colors.CYAN}yt-dlp encontrado. Actualizando a la última versión...{Colors.END}")
        install_ytdlp()  # La función ya actualiza si es necesario
    
    # Verificar nuevamente que el comando esté disponible
    if not check_ytdlp():
        print(f"{Colors.RED}Error: yt-dlp no está disponible después de la instalación. Intenta reiniciar.{Colors.END}")
        sys.exit(1)
    else:
        # Mostrar versión de yt-dlp para confirmar
        try:
            ver_yt = subprocess.run(['yt-dlp', '--version'], capture_output=True, text=True).stdout.strip()
            print(f"{Colors.GREEN}✓ yt-dlp {ver_yt} disponible{Colors.END}")
        except:
            print(f"{Colors.GREEN}✓ yt-dlp disponible{Colors.END}")
    
    # Verificar mpv
    if not check_mpv():
        print(f"\n{Colors.YELLOW}⚠️ mpv no encontrado. Intentando instalar...{Colors.END}")
        if sistema == 'linux':
            if not install_mpv_linux():
                print(f"{Colors.RED}No se pudo instalar mpv. Instálalo manualmente con el gestor de paquetes.{Colors.END}")
                sys.exit(1)
        elif sistema == 'darwin':
            if not install_mpv_macos():
                print(f"{Colors.RED}No se pudo instalar mpv. Instálalo manualmente con 'brew install mpv'.{Colors.END}")
                sys.exit(1)
        elif sistema == 'windows':
            install_mpv_windows()
            print(f"{Colors.YELLOW}Después de instalar mpv, ejecuta este script nuevamente.{Colors.END}")
            sys.exit(1)
    else:
        print(f"{Colors.GREEN}✓ mpv disponible{Colors.END}")
    
    # Verificar que existe xonitube.py
    if not check_xonitube():
        print(f"\n{Colors.RED}❌ No se encuentra xonitube.py en este directorio.{Colors.END}")
        sys.exit(1)
    
    # Ejecutar xonitube.py
    print(f"\n{Colors.BOLD}🚀 Iniciando XONITUBE...{Colors.END}")
    print(f"{Colors.CYAN}Presiona Ctrl+C para salir.{Colors.END}")
    print("-"*50)
    try:
        python_cmd = get_python_command()
        subprocess.run(python_cmd + ['xonitube.py'])
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}🛑 Programa detenido por el usuario.{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error ejecutando xonitube.py: {e}{Colors.END}")
    
    print(f"\n{Colors.GREEN}Gracias por usar XONITUBE 2026{Colors.END}")
    if sistema != 'windows':
        input(f"{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Saliendo...{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}Error inesperado: {e}{Colors.END}")
