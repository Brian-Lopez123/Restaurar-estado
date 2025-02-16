import pickle
import os
import time

ESTADO_ARCHIVO = "estado.pkl"

def guardar_estado(estado):
    """Guarda el estado de ejecución en un archivo."""
    with open(ESTADO_ARCHIVO, "wb") as f:
        pickle.dump(estado, f)

def cargar_estado():
    """Carga el estado de ejecución si existe un archivo guardado."""
    if os.path.exists(ESTADO_ARCHIVO):
        with open(ESTADO_ARCHIVO, "rb") as f:
            return pickle.load(f)
    return None

def main():
    estado = cargar_estado()
    contador = estado["contador"] if estado else 0
    
    print("Presiona Ctrl+C para salir y guardar el estado.")

    try:
        while True:
            contador += 1
            print(f"Ejecutando... Contador: {contador}")
            time.sleep(1)  # Simula una tarea en ejecución
    except KeyboardInterrupt:
        print("\nInterrupción detectada. Guardando estado...")
        guardar_estado({"contador": contador})
        print("Estado guardado. Puedes reanudar la ejecución más tarde.")

if __name__ == "__main__":
    main()
