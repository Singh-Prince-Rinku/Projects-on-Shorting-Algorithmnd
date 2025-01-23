import time
import random
import matplotlib.pyplot as plt

# Sorting algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Performance analysis
def measure_time(sort_function, arr):
    start_time = time.time()
    if sort_function == quick_sort:
        sort_function(arr)  # Quick sort returns a new list
    else:
        sort_function(arr.copy())  # Copy to avoid in-place changes affecting others
    return time.time() - start_time

# Main performance analyzer
def performance_analyzer():
    dataset_sizes = [100, 500, 1000, 5999, 9999]
    sorting_algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }

    results = {algorithm: [] for algorithm in sorting_algorithms}

    # Analyze performance
    for size in dataset_sizes:
        print(f"\nAnalyzing for dataset size: {size}")
        random_list = [random.randint(0, 10000) for _ in range(size)]
        for name, algorithm in sorting_algorithms.items():
            print(f"Running {name}...")
            elapsed_time = measure_time(algorithm, random_list)
            results[name].append(elapsed_time)

    # Plot results
    plt.figure(figsize=(10, 6))
    for name, times in results.items():
        plt.plot(dataset_sizes, times, label=name)
    plt.xlabel("Dataset Size")
    plt.ylabel("Time (seconds)")
    plt.title("Sorting Algorithm Performance")
    plt.legend()
    plt.grid(True)
    plt.show()

# Run the analyzer
if __name__ == "__main__":
    performance_analyzer()
