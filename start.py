#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XONITUBE 2026 - Lanzador Universal
Este script detecta el sistema, instala dependencias y ejecuta xonitube.py
Genera un archivo .bat en Windows para ejecutar con permisos de administrador
Desarrollado por: Darian Alberto Camacho Salas
"""

import subprocess
import sys
import os
import time
import platform
import threading
import ctypes
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

def is_admin():
    """Verifica si el script se ejecuta como administrador en Windows"""
    if platform.system() == 'Windows':
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    return True

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
                elif 'opensuse' in content:
                    return 'opensuse'
                elif 'antix' in content:
                    return 'antix'
        
        try:
            result = subprocess.run(['lsb_release', '-i'], capture_output=True, text=True)
            if 'Ubuntu' in result.stdout:
                return 'ubuntu'
            elif 'Debian' in result.stdout:
                return 'debian'
            elif 'Fedora' in result.stdout:
                return 'fedora'
            elif 'CentOS' in result.stdout:
                return 'centos'
            elif 'antiX' in result.stdout:
                return 'antix'
        except:
            pass
        
        return 'linux-generico'
    except:
        return 'linux-generico'

def get_python_command():
    """Obtiene el comando Python correcto según el sistema"""
    if get_system() == 'windows':
        return ['python']
    else:
        try:
            subprocess.run(['python3', '--version'], capture_output=True, check=True)
            return ['python3']
        except:
            return ['python']

def check_command(comando):
    """Verifica si un comando existe en el sistema"""
    return shutil.which(comando) is not None

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
║                     XONITUBE 2026 v5.8                      ║
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

def check_pip():
    """Verifica que pip está instalado y funciona"""
    try:
        cmd = [sys.executable, '-m', 'pip', '--version']
        subprocess.run(cmd, capture_output=True, check=True)
        return True
    except:
        return False

def install_pip_linux(distro):
    """Instala pip en Linux según la distribución"""
    print(f"{Colors.YELLOW}Instalando pip en {distro}...{Colors.END}")
    
    try:
        if distro in ['ubuntu', 'debian', 'mint', 'antix']:
            subprocess.run(['sudo', 'apt', 'update'], check=False)
            subprocess.run(['sudo', 'apt', 'install', '-y', 'python3-pip'], check=True)
        elif distro in ['arch', 'manjaro']:
            subprocess.run(['sudo', 'pacman', '-Sy', '--noconfirm', 'python-pip'], check=True)
        elif distro in ['fedora']:
            subprocess.run(['sudo', 'dnf', 'install', '-y', 'python3-pip'], check=True)
        elif distro in ['centos', 'rhel']:
            subprocess.run(['sudo', 'yum', 'install', '-y', 'python3-pip'], check=True)
        elif distro in ['opensuse']:
            subprocess.run(['sudo', 'zypper', 'install', '-y', 'python3-pip'], check=True)
        else:
            print(f"{Colors.RED}Distribución no reconocida para instalación automática de pip{Colors.END}")
            return False
        
        print(f"{Colors.GREEN}pip instalado correctamente{Colors.END}")
        return True
    except Exception as e:
        print(f"{Colors.RED}Error instalando pip: {e}{Colors.END}")
        return False

def check_mpv():
    """Verifica si mpv está instalado"""
    return check_command('mpv')

def check_ytdlp():
    """Verifica si yt-dlp está instalado"""
    return check_command('yt-dlp')

def install_mpv_linux(distro):
    """Instala mpv en Linux según la distribución"""
    print(f"{Colors.YELLOW}Instalando mpv en {distro}...{Colors.END}")
    
    try:
        if distro in ['ubuntu', 'debian', 'mint', 'antix']:
            subprocess.run(['sudo', 'apt', 'update'], check=False)
            subprocess.run(['sudo', 'apt', 'install', '-y', 'mpv'], check=True)
        elif distro in ['arch', 'manjaro']:
            subprocess.run(['sudo', 'pacman', '-Sy', '--noconfirm', 'mpv'], check=True)
        elif distro in ['fedora']:
            subprocess.run(['sudo', 'dnf', 'install', '-y', 'mpv'], check=True)
        elif distro in ['centos', 'rhel']:
            subprocess.run(['sudo', 'yum', 'install', '-y', 'mpv'], check=True)
        elif distro == 'opensuse':
            subprocess.run(['sudo', 'zypper', 'install', '-y', 'mpv'], check=True)
        else:
            print(f"{Colors.RED}Distribución no reconocida para instalación automática de mpv{Colors.END}")
            return False
        
        print(f"{Colors.GREEN}mpv instalado correctamente{Colors.END}")
        return True
    except Exception as e:
        print(f"{Colors.RED}Error instalando mpv: {e}{Colors.END}")
        return False

def install_ytdlp_linux(distro):
    """Instala yt-dlp en Linux según la distribución"""
    print(f"{Colors.YELLOW}Instalando yt-dlp en {distro}...{Colors.END}")
    
    try:
        if distro in ['ubuntu', 'debian', 'mint', 'antix']:
            subprocess.run(['sudo', 'apt', 'update'], check=False)
            subprocess.run(['sudo', 'apt', 'install', '-y', 'yt-dlp'], check=True)
        elif distro in ['arch', 'manjaro']:
            subprocess.run(['sudo', 'pacman', '-Sy', '--noconfirm', 'yt-dlp'], check=True)
        elif distro in ['fedora']:
            subprocess.run(['sudo', 'dnf', 'install', '-y', 'yt-dlp'], check=True)
        else:
            # Usar pip como respaldo
            if not check_pip():
                install_pip_linux(distro)
            subprocess.run([sys.executable, '-m', 'pip', 'install', 'yt-dlp'], check=True)
        
        print(f"{Colors.GREEN}yt-dlp instalado correctamente{Colors.END}")
        return True
    except Exception as e:
        print(f"{Colors.RED}Error instalando yt-dlp: {e}{Colors.END}")
        return False

def install_mpv_macos():
    """Instala mpv en macOS usando Homebrew"""
    print(f"{Colors.YELLOW}Instalando mpv en macOS...{Colors.END}")
    
    if not check_command('brew'):
        print(f"{Colors.RED}Homebrew no está instalado{Colors.END}")
        print("  Instala Homebrew desde: https://brew.sh/")
        return False
    
    try:
        subprocess.run(['brew', 'install', 'mpv'], check=True)
        print(f"{Colors.GREEN}mpv instalado correctamente{Colors.END}")
        return True
    except Exception as e:
        print(f"{Colors.RED}Error instalando mpv: {e}{Colors.END}")
        return False

def install_ytdlp_macos():
    """Instala yt-dlp en macOS"""
    print(f"{Colors.YELLOW}Instalando yt-dlp en macOS...{Colors.END}")
    
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'yt-dlp', '--user'], check=True)
        print(f"{Colors.GREEN}yt-dlp instalado correctamente{Colors.END}")
        return True
    except Exception as e:
        print(f"{Colors.RED}Error instalando yt-dlp: {e}{Colors.END}")
        return False

def install_mpv_windows():
    """Muestra instrucciones para instalar mpv en Windows"""
    print(f"{Colors.YELLOW}mpv no está instalado{Colors.END}")
    print("  Instrucciones para Windows:")
    print("  1. Descarga mpv desde: https://mpv.io/installation/")
    print("  2. Extrae el archivo .7z en C:\\mpv")
    print("  3. Agrega C:\\mpv a tu PATH del sistema")
    print("  4. Reinicia la terminal")
    return False

def install_ytdlp_windows():
    """Instala yt-dlp en Windows usando pip"""
    print(f"{Colors.YELLOW}Instalando yt-dlp en Windows...{Colors.END}")
    
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'yt-dlp'], check=True)
        print(f"{Colors.GREEN}yt-dlp instalado correctamente{Colors.END}")
        return True
    except Exception as e:
        print(f"{Colors.RED}Error instalando yt-dlp: {e}{Colors.END}")
        return False

def check_dependencies():
    """Verifica las dependencias necesarias"""
    print(f"\n{Colors.BOLD}Verificando dependencias para XONITUBE...{Colors.END}")
    
    # Verificar mpv
    if check_mpv():
        print(f"{Colors.GREEN}  - mpv OK{Colors.END}")
        mpv_ok = True
    else:
        print(f"{Colors.YELLOW}  - mpv (faltante){Colors.END}")
        mpv_ok = False
    
    # Verificar yt-dlp
    if check_ytdlp():
        print(f"{Colors.GREEN}  - yt-dlp OK{Colors.END}")
        ytdlp_ok = True
    else:
        print(f"{Colors.YELLOW}  - yt-dlp (faltante){Colors.END}")
        ytdlp_ok = False
    
    return mpv_ok, ytdlp_ok

def install_all_dependencies(mpv_falta, ytdlp_falta):
    """Instala todas las dependencias faltantes según el sistema"""
    sistema = get_system()
    distro = get_linux_distro()
    
    print(f"\n{Colors.BOLD}Instalando dependencias faltantes...{Colors.END}")
    
    # Primero asegurar pip si es necesario (para yt-dlp)
    if sistema == 'linux' and ytdlp_falta:
        if not check_pip():
            if not install_pip_linux(distro):
                print(f"{Colors.YELLOW}No se pudo instalar pip. Continuando...{Colors.END}")
    
    success = True
    
    if sistema == 'linux':
        if mpv_falta:
            if not install_mpv_linux(distro):
                success = False
        if ytdlp_falta:
            if not install_ytdlp_linux(distro):
                success = False
    
    elif sistema == 'darwin':
        if mpv_falta:
            if not install_mpv_macos():
                success = False
        if ytdlp_falta:
            if not install_ytdlp_macos():
                success = False
    
    elif sistema == 'windows':
        if mpv_falta:
            install_mpv_windows()
            success = False
        if ytdlp_falta:
            if not install_ytdlp_windows():
                success = False
    
    return success

def create_windows_bat():
    """Crea un archivo .bat para ejecutar con permisos de administrador"""
    sistema = get_system()
    if sistema != 'windows':
        return
    
    bat_content = '''@echo off
title XONITUBE 2026 - Reproductor YouTube
color 1F
cls

echo ========================================
echo      XONITUBE 2026 - Reproductor YouTube
echo      Desarrollado por Darian Alberto
echo      Optimizado para 1GB RAM
echo ========================================
echo.

:: Verificar si se ejecuta como administrador
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [AVISO] Se requieren permisos de administrador para instalar dependencias
    echo.
    echo Solicitando permisos...
    echo.
    
    :: Crear script temporal para ejecutar con admin
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\\getadmin.vbs"
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\\getadmin.vbs"
    "%temp%\\getadmin.vbs"
    del "%temp%\\getadmin.vbs"
    exit /B
)

echo [OK] Permisos de administrador obtenidos
echo.

:: Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no esta instalado
    echo.
    echo Descarga Python desde: https://www.python.org/downloads/
    echo IMPORTANTE: Marca "Add Python to PATH" durante la instalacion
    pause
    start https://www.python.org/downloads/
    exit
)

echo [OK] Python instalado
python --version
echo.

:: Verificar e instalar yt-dlp
python -m pip show yt-dlp >nul 2>&1
if errorlevel 1 (
    echo [AVISO] yt-dlp no encontrado. Instalando...
    python -m pip install yt-dlp
    echo [OK] yt-dlp instalado
) else (
    echo [OK] yt-dlp disponible
)
echo.

:: Verificar mpv
where mpv >nul 2>&1
if errorlevel 1 (
    echo [AVISO] mpv no encontrado
    echo.
    echo Instrucciones para instalar mpv:
    echo 1. Descarga mpv desde: https://mpv.io/installation/
    echo 2. Extrae en C:\\mpv
    echo 3. Agrega C:\\mpv a tu PATH del sistema
    echo.
    echo Presiona una tecla para continuar de todas formas...
    pause >nul
) else (
    echo [OK] mpv disponible
)
echo.

:: Iniciar XONITUBE
echo ========================================
echo Iniciando XONITUBE...
echo ========================================
echo.
python start.py

pause
'''
    
    bat_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'XONITUBE_ADMIN.bat')
    with open(bat_path, 'w', encoding='utf-8') as f:
        f.write(bat_content)
    print(f"{Colors.GREEN}Archivo XONITUBE_ADMIN.bat creado - Ejecuta como administrador si hay problemas{Colors.END}")
    
    # También crear un .bat simple sin admin
    simple_bat = '''@echo off
title XONITUBE 2026
color 1F
python start.py
pause
'''
    simple_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'XONITUBE.bat')
    with open(simple_path, 'w', encoding='utf-8') as f:
        f.write(simple_bat)
    print(f"{Colors.GREEN}Archivo XONITUBE.bat creado - Doble clic para ejecutar{Colors.END}")

def mostrar_instrucciones_python():
    """Muestra instrucciones para instalar Python según el sistema"""
    sistema = get_system()
    distro = get_linux_distro()
    
    if sistema == 'windows':
        print(f"   Descarga Python desde: https://www.python.org/downloads/")
        print(f"   IMPORTANTE: Al instalar, marca 'Add Python to PATH'")
        print(f"   Luego cierra y vuelve a abrir la terminal")
    elif sistema == 'linux':
        if distro in ['ubuntu', 'debian', 'mint', 'antix']:
            print(f"   Instala con: sudo apt update && sudo apt install python3 python3-pip")
        elif distro in ['fedora', 'centos']:
            print(f"   Instala con: sudo dnf install python3 python3-pip")
        elif distro in ['arch', 'manjaro']:
            print(f"   Instala con: sudo pacman -S python python-pip")
        else:
            print(f"   Instala Python 3 desde: https://www.python.org/downloads/")
    elif sistema == 'darwin':
        print(f"   Instala con: brew install python3")
        print(f"   O descarga desde: https://www.python.org/downloads/")

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
    print(f"{Colors.BOLD}Ruta:{Colors.END} {os.path.dirname(os.path.abspath(__file__))}")
    
    # Crear archivos .bat para Windows
    if sistema == 'windows':
        create_windows_bat()
        print()
    
    # Verificar Python
    if not check_python():
        print(f"\n{Colors.RED}Error: Python no esta instalado o no esta en el PATH{Colors.END}")
        mostrar_instrucciones_python()
        input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")
        return
    
    # Mostrar versión de Python
    python_version = subprocess.run(get_python_command() + ['--version'], 
                                   capture_output=True, text=True).stdout.strip()
    print(f"{Colors.BOLD}Python:{Colors.END} {python_version}")
    
    # Verificar pip en Linux (opcional, se puede instalar)
    if sistema == 'linux' and not check_pip():
        print(f"\n{Colors.YELLOW}pip no encontrado. Intentando instalar...{Colors.END}")
        install_pip_linux(distro)
    
    # Verificar dependencias
    mpv_falta, ytdlp_falta = check_dependencies()
    
    # Instalar dependencias si faltan
    if mpv_falta or ytdlp_falta:
        print(f"\n{Colors.YELLOW}Faltan dependencias{Colors.END}")
        
        if sistema == 'windows':
            print(f"\n{Colors.YELLOW}Se recomienda ejecutar XONITUBE_ADMIN.bat como administrador{Colors.END}")
            print(f"   para instalar las dependencias automaticamente")
            respuesta = input(f"Intentar instalar ahora? (s/n): ")
        else:
            respuesta = input(f"Instalar ahora? (s/n): ")
        
        if respuesta.lower() == 's':
            if not install_all_dependencies(mpv_falta, ytdlp_falta):
                print(f"\n{Colors.YELLOW}Continuando a pesar de errores...{Colors.END}")
        else:
            print(f"\n{Colors.YELLOW}No se instalaran dependencias. Puede haber errores.{Colors.END}")
            if sistema == 'windows':
                print(f"   Ejecuta XONITUBE_ADMIN.bat como administrador para instalarlas")
    
    # Verificar que existe xonitube.py
    if not os.path.exists('xonitube.py'):
        print(f"\n{Colors.RED}Error: No se encuentra xonitube.py{Colors.END}")
        print(f"   Asegurate de que xonitube.py esta en la misma carpeta")
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

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Saliendo...{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}Error inesperado: {e}{Colors.END}")
        input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")
