#!/usr/bin/env python3

"""Run multiple sorting algorithms, time them, then plot the results."""

import time
import random
import matplotlib.pyplot as plt

def quicksort(values):
    """Sorts a list of values using the quicksort algorithm."""
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

def bubblesort(values):
    """Sorts a list of values using the bubblesort algorithm."""
    for i in range(len(values)):
        for j in range(len(values) - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
    return values

def mergesort(values):
    """Sorts a list of values using the mergesort algorithm."""
    if len(values) <= 1:
        return values
    middle_index = len(values) // 2
    left = values[:middle_index]
    right = values[middle_index:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)

def merge(left, right):
    """Merges two sorted lists into a single sorted list."""
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result.extend(left)
    if right:
        result.extend(right)
    return result

def benchmark(sorting_algorithm, values_length=1024, number_of_runs=1000):
    """Times how long it takes to sort a list of values."""
    total_time = 0
    for _ in range(number_of_runs):
        values = [random.random() for _ in range(values_length)]
        start = time.time()
        sorting_algorithm(values)
        end = time.time()
        total_time += end - start
    return total_time / number_of_runs

def plot_results():
    """Benchmark all three sorting algorithms at 1000 runs and plot the results."""  
    values_lengths = [1000]
    sorting_algorithms = [quicksort, bubblesort, mergesort]
    for sorting_algorithm in sorting_algorithms:
        times = []
        for values_length in values_lengths:
            times.append(benchmark(sorting_algorithm, values_length))
        plt.plot(values_lengths, times, label=sorting_algorithm.__name__)
    plt.legend()
    plt.xlabel('Number of values')
    plt.ylabel('Time (seconds)')
    plt.show()

if __name__ == '__main__':
    plot_results()

