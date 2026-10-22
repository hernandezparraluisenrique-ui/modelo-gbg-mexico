#!/usr/bin/env python3
"""
PIPELINE MAESTRO - Modelo GBG México
Ejecuta todo el flujo: calibración -> escenarios -> reporte final
"""

import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SCRIPTS = RAIZ / "scripts"

# Orden de ejecución (dependencias)
PIPELINE = [
    ("1. Calibración parámetros (Laplace)", "calibrar_parametros.py"),
    ("2. Escenarios liberación (Monte Carlo)", "analisis_escenarios_liberacion.py"),
    ("3. Finalizar entrega (reinfestación + reporte + gráficos)", "finalizar_entrega.py"),
]

def run_script(nombre, script):
    ruta = SCRIPTS / script
    print(f"\n{'='*60}")
    print(f"EJECUTANDO: {nombre}")
    print(f"Script: {script}")
    print(f"{'='*60}")
    
    try:
        # Usar el mismo python que está corriendo este script
        result = subprocess.run(
            [sys.executable, str(ruta)],
            cwd=str(RAIZ),
            env={**__import__("os").environ, "PYTHONPATH": "."},
            capture_output=True,
            text=True,
            timeout=600,  # 10 min por script
        )
        
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
            
        if result.returncode == 0:
            print(f"\nOK {nombre} - EXITOSO")
            return True
        else:
            print(f"\nFAIL {nombre} - FALLÓ (código {result.returncode})")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"\nFAIL {nombre} - TIMEOUT (>10 min)")
        return False
    except Exception as e:
        print(f"\nFAIL {nombre} - ERROR: {e}")
        return False


def main():
    print("=" * 60)
    print("PIPELINE COMPLETO - MODELO GBG MÉXICO")
    print("=" * 60)
    print(f"Directorio raíz: {RAIZ}")
    print(f"Scripts en: {SCRIPTS}")
    
    # Verificar que existen los scripts
    for nombre, script in PIPELINE:
        if not (SCRIPTS / script).exists():
            print(f"\nFAIL FALTA SCRIPT: {script}")
            return False
    
    print("\nOK Todos los scripts encontrados")
    
    # Ejecutar pipeline
    exitosos = 0
    for nombre, script in PIPELINE:
        if run_script(nombre, script):
            exitosos += 1
        else:
            print(f"\n🛑 Pipeline detenido en: {nombre}")
            return False
    
    # Verificar entregables
    print("\n" + "=" * 60)
    print("VERIFICANDO ENTREGABLES")
    print("=" * 60)
    
    ENTREGABLES = [
        "calibracion_parametros.csv",
        "calibracion_diagnosticos.png",
        "escenarios_liberacion_resultados.csv",
        "escenarios_liberacion_trayectorias.csv",
        "grafico_escenarios.png",
        "RESULTADOS.md",
    ]
    
    for f in ENTREGABLES:
        ruta = RAIZ / f
        if ruta.exists():
            size = ruta.stat().st_size / 1024
            print(f"  OK {f} ({size:.1f} KB)")
        else:
            print(f"  FAIL {f} - NO ENCONTRADO")
    
    print(f"\n{'='*60}")
    print(f"PIPELINE COMPLETADO: {exitosos}/{len(PIPELINE)} pasos exitosos")
    print(f"{'='*60}")
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)