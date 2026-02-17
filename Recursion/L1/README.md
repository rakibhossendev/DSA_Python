# Recursion in Programming

## What is Recursion?

Recursion is a programming technique where a function calls itself in order to solve a problem.

Instead of solving the entire problem at once, recursion breaks the problem into smaller sub-problems of the same type. The function keeps calling itself with smaller inputs until it reaches a stopping condition.

That stopping condition is called the **base case**.

A recursive function must always have:
1. A base case (to stop recursion)
2. A recursive case (where the function calls itself)

---

## Why Do We Use Recursion?

Recursion is used when:

- The problem can naturally be divided into smaller similar sub-problems.
- The structure of the problem is hierarchical (like trees or directories).
- The solution is easier to express recursively than iteratively.

It is commonly used in:

- Mathematical problems (factorial, Fibonacci)
- Tree and graph traversal
- Divide and conquer algorithms (Merge Sort, Quick Sort)
- Backtracking problems
- Parsing nested structures

However, recursion is not always better. Sometimes an iterative solution is more memory-efficient.

---

## How Recursion Works (Concept)

When a function calls itself:

1. The current function call is paused.
2. A new function call is pushed onto the call stack.
3. This continues until the base case is reached.
4. Then the function calls start returning one by one.

This mechanism uses the program’s call stack.

---

## Example 1: Factorial

Mathematical definition:

n! = n × (n - 1) × (n - 2) × ... × 1  
Base case: 0! = 1  

### Recursive Definition

factorial(n):
- If n == 0 → return 1
- Else → return n × factorial(n - 1)

### Python Example

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

### How It Expands

factorial(5)
= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1 * factorial(0)
= 5 * 4 * 3 * 2 * 1 * 1
= 120

---

## Example 2: Fibonacci Sequence

Fibonacci definition:

F(0) = 0  
F(1) = 1  
F(n) = F(n-1) + F(n-2)

### Python Example

```python
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8
```

This is a simple recursive solution, but it is inefficient because it repeats calculations.

---

## Example 3: Recursive Sum of an Array

Problem: Find the sum of a list.

Idea:
- Base case: if list is empty → return 0
- Recursive case: first element + sum of remaining list

```python
def recursive_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + recursive_sum(arr[1:])

print(recursive_sum([1, 2, 3, 4]))  # Output: 10
```

---

## Base Case vs Recursive Case

Every recursive function must clearly define:

Base Case:
Stops recursion.
Without it, the function will call itself infinitely and cause a stack overflow error.

Recursive Case:
Calls the function again with a smaller or simpler input.

If the input does not get smaller or closer to the base case, recursion will never stop.

---

## Call Stack and Memory

Each recursive call uses memory in the call stack.

Example:
If you call factorial(10000), you may get a RecursionError due to stack limit.

Recursion can consume more memory than iteration.

---

## Recursion vs Iteration

Recursion:
- Cleaner and shorter code for some problems
- Uses call stack
- May be slower if not optimized

Iteration:
- Uses loops (for, while)
- More memory-efficient
- Sometimes harder to read for recursive problems

Example (Factorial Iterative Version):

```python
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

---

## When Not to Use Recursion

Do not use recursion when:
- The recursion depth will be very large
- An iterative solution is clearly simpler and more efficient
- The language has strict recursion limits

---

## Important Concepts Related to Recursion

- Tail Recursion
- Stack Frames
- Backtracking
- Divide and Conquer
- Memoization (used to optimize recursive functions)

---

## Summary

Recursion is a powerful technique where a function solves a problem by calling itself on smaller inputs.

To write a correct recursive function:
1. Define a clear base case.
2. Ensure each recursive call moves closer to that base case.
3. Understand how the call stack works.

Recursion makes complex problems easier to think about, especially when the problem has a naturally recursive structure.