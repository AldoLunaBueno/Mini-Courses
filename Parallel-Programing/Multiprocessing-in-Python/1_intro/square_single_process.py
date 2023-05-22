def square(number: float):
    result = number * number
    print(f"The number {number} squares to {result}.")

if __name__=='__main__':
    numbers = [1, 2, 3, 4]
    for number in numbers:
        square(number)