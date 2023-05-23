import time
from multiprocessing import Process, Value, Lock

def add_500_lock(total: Value, lock: Lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        total.value += 5
        print("add")
        lock.release()


def sub_500_lock(total: Value, lock: Lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        total.value -= 5
        print("sub")
        lock.release()

if __name__=='__main__':
    total = Value('i', 500)
    lock = Lock()
    
    process_add = Process(target=add_500_lock, args=(total, lock))
    process_sub = Process(target=sub_500_lock, args=(total, lock))

    process_add.start()
    process_sub.start()

    process_add.join()
    process_sub.join()

    print(total.value)


    