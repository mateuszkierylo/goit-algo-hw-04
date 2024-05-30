# goit-algo-hw-04
Topic 4. Sorting algorithms

This project compares the performance of three sorting algorithms: merge sort, insertion sort, and Timsort (Python's built-in `sorted` function).

## Algorithms

- **Merge Sort**: A divide-and-conquer algorithm with O(n log n) complexity.
- **Insertion Sort**: A simple, comparison-based algorithm with O(n^2) complexity in the average and worst case, but O(n) in the best case.
- **Timsort**: A hybrid sorting algorithm derived from merge sort and insertion sort, designed to perform well on many kinds of real-world data. It has O(n log n) complexity.

## Methodology

We tested the algorithms on random arrays.

Each algorithm was tested on data sets of varying sizes: 100, 1000, and 10000 elements. Execution time was measured using Python's `timeit` module.

## Results

### Random Arrays

#### Size: 100
- **Merge Sort**: 7.800001185387373e-05 seconds
- **Insertion Sort**: 9.941693861037493e-05 seconds
- **Timsort (sorted)**: 7.6669966802001e-06 seconds

#### Size: 1000
- **Merge Sort**: 0.0009420829592272639 seconds
- **Insertion Sort**: 0.012266333098523319 seconds
- **Timsort (sorted)**: 7.529102731496096e-05 seconds

#### Size: 10000
- **Merge Sort**: 0.012514792033471167 seconds
- **Insertion Sort**: 1.254452291992493 seconds
- **Timsort (sorted)**: 0.0009758340893313289 seconds

## Conclusion

The empirical data confirms the theoretical estimates of algorithm complexity. Timsort's combination of merge sort and insertion sort makes it significantly more efficient for a wide range of real-world data. This efficiency is the primary reason why Timsort is used in Python's built-in sorting functions.

For most practical purposes, using Python's built-in `sorted` function is recommended over implementing custom sorting algorithms.


