def get_factorial(num: int) -> int:

    total = 1
    i: int
    for i in range(1, num + 1):
        total *= i
    
    return total


def sum_odd_numbers(num: int) -> int:
    return sum(
        [i for i in range(0, num + 1) if (i%2 != 0)]
    )
