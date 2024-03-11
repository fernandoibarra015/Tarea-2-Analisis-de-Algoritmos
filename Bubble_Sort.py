import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

if __name__ == "__main__":
    n = int(input("Ingrese la cantidad de números a ordenar: "))
    
    # Generar la lista de números aleatorios
    arr = [random.randint(1, 100) for _ in range(n)]
    
    # Iniciar temporizador
    start_time = time.time()
    
    bubble_sort(arr)
    
    # Detener temporizador
    end_time = time.time()
    
    # Calcular y mostrar el tiempo de ejecución
    execution_time = end_time - start_time
    print("Tiempo de ejecución:", execution_time, "segundos")
