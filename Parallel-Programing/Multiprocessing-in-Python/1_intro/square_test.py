from multiprocessing import Process, current_process

processes = [Process]

def square(n: float):
    result = n * n
    process_name = current_process().name
    print(f"Process name: {process_name}")
    print(f"Square of {n} is {result}")

if __name__=='__main__':
    numbers = [1, 2, 3, 4, 5, 6]
    for n in numbers:
        process = Process(target=square, args=(n,))
        processes.append(process)
        process.start()