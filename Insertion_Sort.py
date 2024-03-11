import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    n = int(input("Ingrese la cantidad de números a ordenar: "))
    
    # Generar la lista de números aleatorios
    arr = [random.randint(1, 100) for _ in range(n)]
    
    # Iniciar temporizador
    start_time = time.time()
    
    insertion_sort(arr)
    
    # Detener temporizador
    end_time = time.time()
    
    # Calcular y mostrar el tiempo de ejecución
    execution_time = end_time - start_time
    print("Tiempo de ejecución:", execution_time, "segundos")
