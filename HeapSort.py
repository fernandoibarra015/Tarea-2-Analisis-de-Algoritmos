import random
import time

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

if __name__ == "__main__":
    n = int(input("Ingrese la cantidad de números a ordenar: "))
    
    # Generar la lista de números aleatorios
    arr = [random.randint(1, 100) for _ in range(n)]
    
    # Iniciar temporizador
    start_time = time.time()
    
    heap_sort(arr)
    
    # Detener temporizador
    end_time = time.time()
    
    # Calcular y mostrar el tiempo de ejecución
    execution_time = end_time - start_time
    print("Tiempo de ejecución:", execution_time, "segundos")
