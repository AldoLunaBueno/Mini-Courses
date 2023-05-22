import os
from multiprocessing import Process, current_process

def square(number: float):
    result = number * number

    # Usamos el módulo "os" en Python para imprimir el id del proceso 
    # asignado a la llamada de esta función por el sistema operativo.
    #process_id = os.getpid()
    #print(f"Process ID: {process_id}")

    # Tambíen podemos usar la función current_process() para obtener
    # el nombre del objeto Process.
    process_name = current_process().name
    print(f"Process name: {process_name}")

    print(f"The number {number} squares to {result}.")

if __name__=='__main__':

    processes = []
    numbers = [1, 2, 3, 4, 5, 6]

    for number in numbers:
        process = Process(target=square, args=(number,)) # args = <tuple>
        processes.append(process)

        # Los procesos se generan creando un objeto Process
        # y llamando luego su método start() 
        process.start()
