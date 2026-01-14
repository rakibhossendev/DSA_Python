# DSA Class 2  
## TLE (Time Limit Exceeded) Error

### 📌 What is TLE?
TLE stands for **Time Limit Exceeded**.  
If a program does not finish execution within the given time limit (e.g., 1s or 2s),
the judge rejects it with a TLE error.

In simple words:
> The logic is correct, but the program is **too slow**.

---

### ⏱️ Why Does TLE Happen?
TLE usually occurs due to the following reasons:

1. ❌ Using unnecessary loops  
2. ❌ Nested loops (loop inside another loop)  
3. ❌ Inefficient algorithms for large input  
4. ❌ Recursive solutions without optimization  
5. ❌ Repeating the same computation again and again  

---

### 🧠 Example

Assume `n = 10^7`

👉 Time Complexity: O(n²)

✅ Optimized Code
#### ❌ Bad Code (Will cause TLE)
```python
for i in range(n):
    for j in range(n):
        pass
```

👉 Time Complexity: O(n)

## 📊 Time Complexity vs TLE Risk

| Time Complexity | Status for Large Input |
|-----------------|------------------------|
| O(1)            | Safe ✅                |
| O(log n)        | Safe ✅                |
| O(n)            | Usually Safe ✅        |
| O(n log n)      | Mostly Safe ⚠️        |
| O(n²)           | Risky ❌               |
| O(2ⁿ)           | TLE Guaranteed ❌❌    |

## 🛠️ How to Avoid TLE?
- Choose efficient algorithms
- Always calculate time complexity
- Reduce nested loops
- Remove unnecessary operations
- Use optimization techniques (precomputation, caching, etc.)


## 🔑 Key Takeaway
***Correct Logic + Poor Time Complexity = TLE***
Before submitting any solution, ask yourself:
***“Will this solution work fast for very large input?”***


## 📚 Next Class
- ➡️ Optimized Thinking & Time Complexity Practice

