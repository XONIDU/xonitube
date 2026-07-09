@echo off
title XONITUBE 2026 - Reproductor de YouTube desde Terminal
color 0A

:: ============================================================
:: IR AL DIRECTORIO DONDE ESTA EL SCRIPT .BAT
:: ============================================================
cd /d "%~dp0"

:: ============================================================
:: SOLICITAR PERMISOS DE ADMINISTRADOR
:: ============================================================
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Solicitando permisos de administrador...
    echo.
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B
)

:: ============================================================
:: VERIFICAR QUE start.py EXISTE
:: ============================================================
if not exist "%~dp0start.py" (
    echo [ERROR] No se encuentra start.py en esta carpeta
    echo.
    echo Ruta actual: %~dp0
    echo.
    echo Asegurate de que start.py esta en la misma carpeta que este .bat
    echo.
    pause
    exit /B
)

:: ============================================================
:: EJECUTAR start.py CON PERMISOS DE ADMINISTRADOR
:: ============================================================
cls
echo ============================================================
echo           XONITUBE 2026 - Reproductor de YouTube
echo              (Modo Administrador)
echo ============================================================
echo.
echo [OK] Permisos de administrador obtenidos
echo.
echo [INFO] Directorio de trabajo: %~dp0
echo.
echo Iniciando XONITUBE...
echo.
echo [INFO] Buscador y reproductor de YouTube desde terminal
echo [INFO] Optimizado para equipos de bajos recursos (1GB RAM)
echo [INFO] Descargas en: %%USERPROFILE%%\Videos\XoniTube\
echo.
echo CONTROLES DURANTE REPRODUCCION:
echo   ← →  : Retroceder/Avanzar 5s
echo   Space : Pausa/Reanudar
echo   ↑ ↓  : Volumen
echo   q    : Salir
echo   Ctrl+C : Volver al menu
echo.
echo ============================================================
echo.

python start.py

pause