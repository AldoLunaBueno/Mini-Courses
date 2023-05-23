import time
from multiprocessing import Process, Value, Lock

def add_500_no_lock(total: Value):
    for i in range(100):
        time.sleep(0.01)
        total.value += 5
def sub_500_no_lock(total: Value):
    for i in range(100):
        time.sleep(0.01)
        total.value -= 5

if __name__=='__main__':
    total = Value('i', 500)
    
    process_add = Process(target=add_500_no_lock, args=(total,))
    process_sub = Process(target=sub_500_no_lock, args=(total,))

    process_add.start()
    process_sub.start()

    process_add.join()
    process_sub.join()

    print(total.value)


    