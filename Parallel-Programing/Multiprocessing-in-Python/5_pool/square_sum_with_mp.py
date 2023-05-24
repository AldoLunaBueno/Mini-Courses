# -*- coding: utf-8 -*-

import time
from multiprocessing import Process, Pool

def square_sum(n: int) -> int:
    s = 0
    for i in range(n):
        s += i*i
    return s
def square_sum_no_mp(numbers: list[int]) -> list[int]:
    start_time = time.time()
    result = [square_sum(number) for number in numbers]
    end_time = time.time()
    print(f"La función sin multiprocesamiento tardó: {end_time - start_time}")
    return result
def square_sum_with_mp(numbers: list[int]):
    start_time = time.time()
    pool = Pool(5)
    result = pool.map(square_sum, numbers)
    pool.close()
    pool.join()
    end_time = time.time()
    print(f"La función con multiprocesamiento tardó: {end_time - start_time}")
    return result

if __name__=='__main__':
    numbers = range(20000)    
    square_sum_with_mp(numbers)
    square_sum_no_mp(numbers)

