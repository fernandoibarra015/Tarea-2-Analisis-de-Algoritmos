import random
import time

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

if __name__ == "__main__":
    n = int(input("Ingrese la cantidad de números a ordenar: "))
    
    # Generar la lista de números aleatorios
    arr = [random.randint(1, 100) for _ in range(n)]
    
    # Iniciar temporizador
    start_time = time.time()
    
    quick_sort(arr, 0, len(arr) - 1)
    
    # Detener temporizador
    end_time = time.time()
    
    # Calcular y mostrar el tiempo de ejecución
    execution_time = end_time - start_time
    print("Tiempo de ejecución:", execution_time, "segundos")
