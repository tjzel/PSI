from functools import reduce


def foo(numbers: list[int]):
    sum = reduce(lambda acc, el: acc + el, numbers, 0)
    max = max(list)
    avg = sum / len(list)
    return [sum, max, avg]
