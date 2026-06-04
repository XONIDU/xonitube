#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XONITUBE 2026 - Lanzador Universal
Reproductor de YouTube desde terminal para 1GB RAM
Incluye múltiples estrategias de instalación para todas las distribuciones
Desarrollador: Darian Alberto Camacho Salas
Organización: XONIDU
"""

import subprocess
import sys
import os
import platform
import shutil
import importlib.util
import time
import tempfile

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
        for cmd in ['python3', 'python']:
            try:
                subprocess.run([cmd, '--version'], capture_output=True, check=True)
                return [cmd]
            except:
                continue
        return ['python3']

def get_pip_command():
    # Probar diferentes formas de ejecutar pip
    pip_commands = [
        [sys.executable, '-m', 'pip'],
        ['pip3'],
        ['pip'],
        [sys.executable, '-m', 'pip3'],
        ['python3', '-m', 'pip'],
        ['python', '-m', 'pip']
    ]
    for cmd in pip_commands:
        try:
            subprocess.run(cmd + ['--version'], capture_output=True, check=True)
            return cmd
        except:
            continue
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

def get_script_dir():
    return os.path.dirname(os.path.abspath(__file__))

def get_xonitube_path():
    """Detecta la ruta de xonitube.py en múltiples ubicaciones"""
    script_dir = get_script_dir()
    rutas = [
        os.path.join(script_dir, 'xonitube.py'),
        '/usr/share/xonitube/xonitube.py',
        os.path.join(os.path.expanduser("~"), '.xonitube', 'xonitube.py'),
        os.path.join(os.path.expanduser("~"), 'xonitube', 'xonitube.py'),
        '/usr/local/share/xonitube/xonitube.py',
        os.path.join(os.getcwd(), 'xonitube.py')
    ]
    for r in rutas:
        if os.path.exists(r):
            return r
    return None

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
║                    XONITUBE 2026 v6.6                     ║
║              Reproductor de YouTube desde Terminal        ║
║                   Optimizado para 1GB RAM                 ║
║                                                            ║
║               Sistema detectado: {sistema_texto:<27} ║
║                                                            ║
║               Desarrollado por: Darian Alberto            ║
║                      Camacho Salas                        ║
║                      Organización: XONIDU                 ║
╚══════════════════════════════════════════════════════════════╝{Colors.END}
    """
    print(banner)

def mostrar_ayuda():
    ayuda = f"""
{Colors.BOLD}USO DE XONITUBE:{Colors.END}

  xonitube

{Colors.BOLD}CARACTERISTICAS:{Colors.END}

  ✅ Busca videos desde terminal
  ✅ Reproduce con mpv (backends automaticos)
  ✅ Guarda videos localmente
  ✅ Optimizado para 1GB RAM
  ✅ Sin navegador, sin lag

{Colors.BOLD}COMANDOS DURANTE REPRODUCCION:{Colors.END}

  ← →      - Retroceder/Avanzar 5s
  Space    - Pausa/Reanudar
  ↑ ↓      - Volumen
  q        - Salir de reproduccion
  Ctrl+C   - Volver al menu

{Colors.BOLD}DESCARGAS:{Colors.END}

  Los videos guardados se almacenan en:
  ~/Videos/XoniTube/
    """
    print(ayuda)

# ============================================================================
# Verificación de dependencias del sistema
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
    
    estrategias = []
    if distro == 'debian-based':
        estrategias = [
            ['sudo', 'apt', 'update'],
            ['sudo', 'apt', 'install', '-y', 'python3-pip']
        ]
    elif distro == 'arch-based':
        estrategias = [
            ['sudo', 'pacman', '-S', '--noconfirm', 'python-pip']
        ]
    elif distro == 'fedora':
        estrategias = [
            ['sudo', 'dnf', 'install', '-y', 'python3-pip']
        ]
    elif distro == 'centos':
        estrategias = [
            ['sudo', 'yum', 'install', '-y', 'python3-pip']
        ]
    elif distro == 'opensuse':
        estrategias = [
            ['sudo', 'zypper', 'install', '-y', 'python3-pip']
        ]
    else:
        estrategias = [
            ['sudo', 'apt', 'update'],
            ['sudo', 'apt', 'install', '-y', 'python3-pip']
        ]
    
    try:
        for cmd in estrategias:
            subprocess.run(cmd, check=False)
        return True
    except:
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

def install_pip_macos():
    print(f"{Colors.YELLOW}Instalando pip en macOS...{Colors.END}")
    if shutil.which('brew'):
        try:
            subprocess.run(['brew', 'install', 'python3'], check=True)
            return True
        except:
            pass
    try:
        subprocess.run([sys.executable, '-m', 'ensurepip', '--upgrade'], check=True)
        return True
    except:
        return False

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
    if shutil.which('brew'):
        try:
            subprocess.run(['brew', 'install', 'mpv'], check=True)
            return True
        except:
            return False
    print(f"{Colors.YELLOW}Homebrew no instalado. Instala mpv manualmente: brew install mpv{Colors.END}")
    return False

def install_mpv_windows():
    print(f"{Colors.YELLOW}mpv no encontrado. Instrucciones para Windows:{Colors.END}")
    print("  1. Descarga mpv desde: https://mpv.io/installation/")
    print("  2. Extrae el archivo .7z en C:\\mpv")
    print("  3. Agrega C:\\mpv a tu PATH del sistema")
    print("  4. Reinicia la terminal")
    return False

def install_ytdlp():
    """Instala o actualiza yt-dlp usando múltiples estrategias"""
    sistema = get_system()
    distro = get_linux_distro()
    
    # Estrategias por sistema
    estrategias = []
    
    if sistema == 'linux':
        if distro == 'arch-based':
            estrategias.append(['sudo', 'pacman', '-S', '--noconfirm', 'yt-dlp'])
        elif distro == 'debian-based':
            estrategias.append(['sudo', 'apt', 'install', '-y', 'yt-dlp'])
        elif distro == 'fedora':
            estrategias.append(['sudo', 'dnf', 'install', '-y', 'yt-dlp'])
        elif distro == 'centos':
            estrategias.append(['sudo', 'yum', 'install', '-y', 'yt-dlp'])
        elif distro == 'opensuse':
            estrategias.append(['sudo', 'zypper', 'install', '-y', 'yt-dlp'])
    
    # Estrategias con pip
    if check_pip() or check_python():
        pip_cmd = get_pip_command()
        flags_options = [
            [],
            ['--user'],
            ['--break-system-packages'],
            ['--user', '--break-system-packages']
        ]
        for flags in flags_options:
            estrategias.append(pip_cmd + ['install', '--upgrade', 'yt-dlp'] + flags)
    
    # Estrategia: instalación directa desde GitHub
    if sistema == 'linux':
        estrategias.append([
            'sudo', 'curl', '-L', 
            'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp',
            '-o', '/usr/local/bin/yt-dlp'
        ])
        estrategias.append(['sudo', 'chmod', 'a+rx', '/usr/local/bin/yt-dlp'])
    
    for idx, cmd in enumerate(estrategias, 1):
        print(f"  Intento {idx}: {' '.join(cmd)}")
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if result.returncode == 0:
                print(f"{Colors.GREEN}✓ yt-dlp instalado correctamente{Colors.END}")
                return True
        except subprocess.TimeoutExpired:
            print(f"  Timeout")
        except Exception as e:
            print(f"  Error: {str(e)[:50]}")
    
    return False

# ============================================================================
# Función principal
# ============================================================================
def main():
    if get_system() == 'windows':
        os.system('cls')
    else:
        os.system('clear')
    
    print_banner()
    
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', '/?']:
        mostrar_ayuda()
        if get_system() != 'windows':
            input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")
        return
    
    if not check_python():
        print(f"\n{Colors.RED}❌ Python no esta instalado{Colors.END}")
        sys.exit(1)
    
    ver_py = subprocess.run(get_python_command() + ['--version'], capture_output=True, text=True).stdout.strip()
    print(f"{Colors.BOLD}Python:{Colors.END} {ver_py}")
    
    if not check_pip():
        print(f"\n{Colors.YELLOW}⚠️ Pip no encontrado. Instalando...{Colors.END}")
        sistema = get_system()
        if sistema == 'linux':
            if not install_pip_linux():
                print(f"{Colors.RED}No se pudo instalar pip.{Colors.END}")
                print("   Instala python3-pip manualmente con tu gestor de paquetes")
                sys.exit(1)
        elif sistema == 'darwin':
            if not install_pip_macos():
                print(f"{Colors.RED}No se pudo instalar pip.{Colors.END}")
                sys.exit(1)
        elif sistema == 'windows':
            if not install_pip_windows():
                print(f"{Colors.RED}No se pudo instalar pip. Ejecuta como administrador.{Colors.END}")
                sys.exit(1)
    else:
        print(f"{Colors.GREEN}✓ Pip disponible{Colors.END}")
    
    # Verificar mpv
    if not check_mpv():
        print(f"\n{Colors.YELLOW}⚠️ mpv no encontrado. Intentando instalar...{Colors.END}")
        sistema = get_system()
        if sistema == 'linux':
            if not install_mpv_linux():
                print(f"{Colors.RED}No se pudo instalar mpv. Instálalo manualmente.{Colors.END}")
                sys.exit(1)
        elif sistema == 'darwin':
            if not install_mpv_macos():
                print(f"{Colors.RED}No se pudo instalar mpv. Instálalo manualmente con 'brew install mpv'.{Colors.END}")
                sys.exit(1)
        elif sistema == 'windows':
            install_mpv_windows()
            sys.exit(1)
    else:
        print(f"{Colors.GREEN}✓ mpv disponible{Colors.END}")
    
    # Verificar/instalar yt-dlp
    if not check_ytdlp():
        print(f"\n{Colors.YELLOW}⚠️ yt-dlp no encontrado. Instalando...{Colors.END}")
        if not install_ytdlp():
            print(f"{Colors.RED}No se pudo instalar yt-dlp.{Colors.END}")
            print("   Instálalo manualmente: pip install yt-dlp")
            sys.exit(1)
    else:
        print(f"{Colors.GREEN}✓ yt-dlp disponible{Colors.END}")
        # Opcional: actualizar
        print(f"{Colors.CYAN}Intentando actualizar yt-dlp...{Colors.END}")
        install_ytdlp()
    
    # Buscar xonitube.py
    ruta_xonitube = get_xonitube_path()
    if not ruta_xonitube:
        print(f"\n{Colors.RED}❌ No se encuentra xonitube.py{Colors.END}")
        print("   Buscado en:")
        print("     - Mismo directorio que start.py")
        print("     - /usr/share/xonitube/xonitube.py")
        print("     - ~/.xonitube/xonitube.py")
        print("     - ~/xonitube/xonitube.py")
        sys.exit(1)
    
    xonitube_dir = os.path.dirname(ruta_xonitube)
    print(f"{Colors.GREEN}✓ xonitube.py encontrado en: {xonitube_dir}{Colors.END}")
    
    # Cambiar al directorio y ejecutar
    os.chdir(xonitube_dir)
    print(f"\n{Colors.BOLD}🚀 Iniciando XONITUBE...{Colors.END}")
    print(f"{Colors.CYAN}Presiona Ctrl+C para salir.{Colors.END}")
    print("-"*50)
    
    try:
        python_cmd = get_python_command()
        subprocess.run(python_cmd + [ruta_xonitube])
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}🛑 Programa detenido por el usuario.{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error ejecutando xonitube.py: {e}{Colors.END}")
    
    print(f"\n{Colors.GREEN}Gracias por usar XONITUBE 2026{Colors.END}")
    if get_system() != 'windows':
        input(f"{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Saliendo...{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}Error inesperado: {e}{Colors.END}")
