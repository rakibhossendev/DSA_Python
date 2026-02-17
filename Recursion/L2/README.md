# Recursion Using Parameters

## Introduction

Recursion using parameters refers to a recursive function where important values are passed as arguments during each function call.

Instead of relying on global variables or returning and combining results later, parameter-based recursion passes updated values directly into the next recursive call.

This technique is often used to:

- Accumulate results
- Track progress
- Control recursion flow
- Improve clarity and efficiency

---

## Basic Structure

A recursive function using parameters usually follows this pattern:

1. Base Case → Stops recursion
2. Recursive Case → Calls itself with updated parameters

Example structure:

```python
def function(parameter1, parameter2):
    if base_condition:
        return result
    return function(updated_parameter1, updated_parameter2)
```

The key idea is:
Each recursive call receives modified parameters that move the function closer to the base case.

---

## Example 1: Sum of Numbers Using Accumulator Parameter

Problem:
Find the sum of numbers from 1 to n.

Instead of writing:

sum(n) = n + sum(n - 1)

We use an additional parameter to keep track of the total.

### Python Example

```python
def sum_to_n(n, total=0):
    if n == 0:
        return total
    return sum_to_n(n - 1, total + n)

print(sum_to_n(5))  # Output: 15
```

### How It Works

sum_to_n(5, 0)
→ sum_to_n(4, 5)
→ sum_to_n(3, 9)
→ sum_to_n(2, 12)
→ sum_to_n(1, 14)
→ sum_to_n(0, 15)
→ returns 15

Here:
- n is decreasing
- total is accumulating the result

This avoids adding values after recursion returns.

---

## Example 2: Factorial Using Parameter

Normal recursive factorial:

factorial(n) = n × factorial(n - 1)

Parameter-based factorial using accumulator:

```python
def factorial(n, result=1):
    if n == 0:
        return result
    return factorial(n - 1, result * n)

print(factorial(5))  # Output: 120
```

### Execution Flow

factorial(5, 1)
→ factorial(4, 5)
→ factorial(3, 20)
→ factorial(2, 60)
→ factorial(1, 120)
→ factorial(0, 120)
→ returns 120

This style is closer to tail recursion.

---

## Example 3: Reverse a String Using Parameter

Problem:
Reverse a string recursively.

We pass an extra parameter to store the reversed result.

```python
def reverse_string(s, reversed_str=""):
    if len(s) == 0:
        return reversed_str
    return reverse_string(s[1:], s[0] + reversed_str)

print(reverse_string("hello"))  # Output: olleh
```

Explanation:
- Each call removes the first character
- That character is added to the front of reversed_str
- Continues until the string is empty

---

## Example 4: Count Digits in a Number

```python
def count_digits(n, count=0):
    if n == 0:
        return count
    return count_digits(n // 10, count + 1)

print(count_digits(12345))  # Output: 5
```

Here:
- n gets smaller by dividing by 10
- count increases in each call

---

## Why Use Parameters in Recursion?

Using parameters helps:

1. Avoid global variables
2. Keep state explicitly controlled
3. Improve readability
4. Make tail recursion possible
5. Reduce work after recursion returns

It often leads to more efficient solutions.

---

## Tail Recursion Concept

When a recursive function returns directly from the recursive call without extra computation, it is called tail recursion.

Example:

```python
return factorial(n - 1, result * n)
```

There is no multiplication after the recursive call.
The work is done before calling the function again.

Some languages optimize tail recursion, but Python does not.

---

## Common Mistakes

1. Forgetting the base case
2. Not updating parameters correctly
3. Causing infinite recursion
4. Losing track of the accumulated value

Always make sure:
- Parameters move toward the base condition
- The base case returns the correct result

---

## Parameter Recursion vs Normal Recursion

Normal Recursion:
- Combines results after returning
- Example: return n + sum(n - 1)

Parameter-Based Recursion:
- Passes accumulated result forward
- Example: return sum(n - 1, total + n)

Parameter-based recursion often reduces extra operations during the return phase.

---

## Summary

Recursion using parameters is a structured approach where values are passed and updated during each recursive call.

Key Points:

- Always define a base case
- Update parameters in each call
- Move closer to termination
- Use accumulator parameters for cleaner logic

This technique makes recursive functions more powerful, organized, and efficient.
