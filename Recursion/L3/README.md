# Recursion: Parameterized and Functional Approaches in Python

## Introduction

Recursion is a technique where a function calls itself to solve a problem.

There are mainly two styles of recursion:

1. Parameterized Recursion
2. Functional Recursion

Both approaches solve problems recursively, but they differ in how results are handled.

---

# 1. Parameterized Recursion

## Definition

In parameterized recursion, we pass the result (or state) as a parameter to the recursive function.

The result is carried forward through arguments, and the final answer is usually printed or returned at the base case.

The function does not depend on returned values from deeper recursive calls.

---

## Example 1: Sum from 1 to N (Parameterized)

```python
def func(sum, i, n):
    if i > n:
        print(sum)
        return
    func(sum + i, i + 1, n)

func(0, 1, 10)
```

### How It Works

Initial Call:
func(0, 1, 10)

Flow:
- func(0+1, 2, 10)
- func(1+2, 3, 10)
- func(3+3, 4, 10)
- ...
- func(55, 11, 10)

When i > n:
print(sum)

Output:
55

### Key Idea

- sum accumulates the total.
- i increases each time.
- Base case stops recursion when i > n.
- The result is passed forward as a parameter.

This approach is called accumulator-based recursion.

---

## Characteristics of Parameterized Recursion

- Uses extra parameters to store intermediate results
- Often does not return values from recursive calls
- Useful when tracking state
- Similar to tail recursion style

---

# 2. Functional Recursion

## Definition

In functional recursion, the function returns values.
The final answer is built by combining results of recursive calls.

Each recursive call returns a value to the previous call.

---

## Example 2: Sum from 1 to N (Functional)

```python
def f(n):
    if n == 1:
        return 1
    x = n + f(n - 1)
    return x

print(f(10))
```

### How It Works

f(10)
= 10 + f(9)
= 10 + 9 + f(8)
= 10 + 9 + 8 + ...
= 10 + 9 + ... + 1

Returns:
55

### Execution Breakdown

f(1) returns 1  
f(2) returns 2 + 1 = 3  
f(3) returns 3 + 3 = 6  
f(4) returns 4 + 6 = 10  
...  
f(10) returns 55  

Each function waits for the smaller function to return before computing its result.

---

## Characteristics of Functional Recursion

- Returns values from recursive calls
- Combines results after recursion returns
- Easier to understand for mathematical definitions
- Uses call stack heavily

---

# Comparison: Parameterized vs Functional Recursion

Parameterized Recursion:
- Result is passed forward
- Often prints or returns at base case
- No pending operations after recursive call
- Closer to tail recursion

Functional Recursion:
- Result is returned upward
- Combines results after recursive call
- Each call waits for child call
- More natural for mathematical expressions

---

# Call Stack Behavior

In Functional Recursion:

Each recursive call waits until the deeper call finishes.
This creates a chain of pending operations in memory.

In Parameterized Recursion:

The result is updated before the next call.
There is no extra computation after returning.

---

# Common Mistakes in Recursion

1. Missing base case
2. Incorrect base condition
3. Not reducing the problem size
4. Infinite recursion
5. Stack overflow for large inputs

Always ensure:
- The recursive step moves closer to the base case
- The base case is reachable

---

# Conclusion

Recursion is a powerful problem-solving technique.

There are two main styles:

1. Parameterized Recursion  
   - Uses arguments to carry state  
   - Often prints or returns in base case  

2. Functional Recursion  
   - Uses return values  
   - Builds solution while returning  

Understanding both styles helps in writing clean recursive algorithms and choosing the right approach depending on the problem.