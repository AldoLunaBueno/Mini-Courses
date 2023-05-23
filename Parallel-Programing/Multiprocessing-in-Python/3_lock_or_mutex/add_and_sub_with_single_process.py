import time

def add_500(total: int) -> int:
    for i in range(100):
        time.sleep(0.01)
        total += 50
    return total
def sub_500(total: int) -> int:
    for i in range(100):
        time.sleep(0.01)
        total -= 5
    return total

if __name__=='__main__':
    total = 500
    total = add_500(total)
    total = sub_500(total)
    print(total)