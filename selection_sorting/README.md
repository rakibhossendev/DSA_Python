# Selection Sort Implementation in Python

## Overview

This project contains a basic implementation of the Selection Sort algorithm in Python.

Selection Sort is a simple comparison-based sorting algorithm. It repeatedly finds the minimum element from the unsorted portion of the list and places it at the beginning.

---

## How Selection Sort Works

1. Start from the first index.
2. Assume the current index holds the minimum value.
3. Traverse the remaining unsorted portion of the list.
4. If a smaller element is found, update the minimum index.
5. Swap the smallest found element with the current index.
6. Move to the next index and repeat the process.
7. Continue until the entire list is sorted.

---

## Time Complexity

Worst Case: O(n²)  
Average Case: O(n²)  
Best Case: O(n²)  

Selection Sort always performs the same number of comparisons regardless of input order.

---

## Space Complexity

O(1)

It is an in-place sorting algorithm since it does not require extra memory proportional to input size.

---

## Python Implementation

```python
def selectionSorting(nums):
    n = len(nums)
    for i in range(0, n):
        min_index = i
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


nums = [10,7,6,5,8,9,3,2,1,4]
sorted_l = selectionSorting(nums)
print(sorted_l)		
```
## Example
### Input:
```
[10,7,6,5,8,9,3,2,1,4]
```
### Output:
```
[1,2,3,4,5,6,7,8,9,10]
```

## Key Learning Points
- Understand nested loops.
- Understand index tracking.
- Understand in-place swapping.
- Learn time complexity growth (quadratic pattern).
- Practice manual dry run for deeper understanding.

## When to Use Selection Sort
- Selection Sort is mainly used for educational purposes to understand sorting logic. It is not efficient for large datasets compared to advanced algorithms like Merge Sort or Quick Sort.
