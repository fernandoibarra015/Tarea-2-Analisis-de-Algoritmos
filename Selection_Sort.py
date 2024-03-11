import random
import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == "__main__":
    n = int(input("Ingrese la cantidad de números a ordenar: "))
    
    # Generar la lista de números aleatorios
    arr = [random.randint(1, 100) for _ in range(n)]
    
    # Iniciar temporizador
    start_time = time.time()
    
    selection_sort(arr)
    
    # Detener temporizador
    end_time = time.time()
    
    # Calcular y mostrar el tiempo de ejecución
    execution_time = end_time - start_time
    print("Tiempo de ejecución:", execution_time, "segundos")
