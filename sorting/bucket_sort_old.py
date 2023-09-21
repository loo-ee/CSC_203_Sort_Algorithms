from sorting.merge_sort import merge_sort


def bucket_sort(array: list):
    buckets = []
    sorted_array = []
    arr_len = len(array)
    max_val = max(array)
    min_val = min(array)
    arr_range = max_val - min_val + 1

    for i in range(arr_range):
        buckets.append([])

    for i in range(arr_len):
        el_index = array[i] - min_val
        buckets[el_index].append(array[i])

    for i in range(arr_len):
        merge_sort(buckets[i], 0)

    for i in range(len(buckets)):
        if len(buckets[i]) == 0:
            continue

        sorted_array += buckets[i]

    print(buckets)

    return sorted_array


def run(array: list):
    print('Array before sorting: ', array)
    array = bucket_sort(array)
    print('Array after sorting: ', array)
    