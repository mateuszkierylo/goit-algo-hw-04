import random
import timeit

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def measure_time(sort_fn, arr):
    return timeit.timeit(lambda: sort_fn(arr.copy()), number=1)

def create_random_array(size):
    return [random.randint(0, 100000) for _ in range(size)]

def run_tests():
    sizes = [100, 1000, 10000]
    for size in sizes:
        print(f"\nTesting with size: {size}")
        random_array = create_random_array(size)

        print("\nRandom array:")
        print("Merge Sort:", measure_time(merge_sort, random_array))
        print("Insertion Sort:", measure_time(insertion_sort, random_array))
        print("Timsort (sorted):", measure_time(sorted, random_array))

if __name__ == "__main__":
    run_tests()
