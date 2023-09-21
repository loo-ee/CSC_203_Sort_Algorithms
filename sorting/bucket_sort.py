from colorama import Fore
from sorting.merge_sort import merge_sort
from util.util import colored_array_print

def print_buckets(buckets: [[int]]):
    for bucket in buckets:
        if len(bucket) != 0:
            print(bucket, end="   ")

    print()


def bucket_sort(array: list):
    min_val = min(array)
    max_val = max(array)
    n = len(array)  
    num_buckets = n
    buckets = [[] for _ in range(num_buckets)]

    for num in array:
        index = int((num - min_val) * (num_buckets - 1) / (max_val - min_val))
        buckets[index].append(num)

    print()
    colored_array_print("SCATTERING", Fore.BLUE, False)
    print()
    print_buckets(buckets)

    for bucket in buckets:
        bucket.sort()

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
        
    print()
    colored_array_print("SORTING", Fore.GREEN, False)
    print()
    print_buckets(buckets)

    return sorted_arr


def run(array: list):
    print('Array before sorting: ', array)
    array = bucket_sort(array)
    print('\nArray after sorting: ', array)
