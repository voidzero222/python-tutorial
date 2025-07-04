import random
import time
from collections.abc import Iterable 
from typing import Callable
type Func = Callable[[int, list[int]], float | int | None]

def lookup_linear(value:int , arr:list[int])-> int:
    i = 0
    for item in arr:
        if item == value:
            return i
        else:
            i = i+1
    return -1
            
            

def lookup_index(value:int,arr:list[int])-> int:
    return arr.index(value)


def lookup_random(value:int,arr:list[int]) -> int:
    while True:
        i = random.randrange(len(arr)) 
        if arr[i] == value:
            return i 


def lookup_binary_no_sort(value:int, arr:list[int]) ->int:
    length = len(arr)
    half = length // 2
    last_half_half = half
    while True:
        num = arr[half]
        if num == value:
            return half
        elif num < value:
            last_half_half = max(round(last_half_half / 2), 1)
            half += last_half_half
        else:
            last_half_half = max(round(last_half_half / 2), 1)
            half -= last_half_half


def lookup_binary_sort(value:int, arr:list[int])->int:
    random.shuffle(arr)
    return lookup_binary_no_sort(value, sorted(arr))


def benchmark(func:Func)-> list[float]:
    times = []
    for item_amount in [10, 100, 1_000, 10_000, 1_000_000]:
        tries = 100 
        times1 = [] 
        for _ in range(tries):
            start_time = time.time()
            items = list(range(item_amount))
            func(random.randrange(item_amount),items)
            time_taken = time.time() - start_time
            times1.append(time_taken)

        time_taken_total = sum(times1) / tries
        times.append(time_taken_total)

    return times


def print_benchmark_results(func:Func)-> None:
    results = benchmark(func)
    amounts = [10, 100, 1_000, 10_000, 1_000_000]
    i = 0
    print(f"Results for: {func.__name__}")
    for result in results:
        print(f"Result for {amounts[i]}: {result:.10f}")
        i += 1
    print()
    


print_benchmark_results(lookup_linear)
print_benchmark_results(lookup_index)
print_benchmark_results(lookup_random)
print_benchmark_results(lookup_binary_sort)
print_benchmark_results(lookup_binary_no_sort)
