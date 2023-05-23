import time
from multiprocessing import Process, current_process

def square(numbers: list[float]):
    for n in numbers:
        time.sleep(0.5)
        result = n * n
        print(f"The number {n} squares to {result}")

if __name__=='__main__':
    processes: list[Process] = []
    numbers = range(20)
    for i in range(10):
        process = Process(target=square, args=(numbers,))
        processes.append(process)

        process.start()

    for process in processes:
        process.join()

    print("Multiprocessing complete")
