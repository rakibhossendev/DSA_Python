# DSA Class 4

## Extraction of digites

# DSA Class 4  
## Extraction of Digits (Digit Extraction)

### 📌 What is Digit Extraction?
Digit Extraction মানে হলো একটি সংখ্যার প্রতিটি digit আলাদা আলাদা করে বের করা।  
DSA–তে এটি খুবই গুরুত্বপূর্ণ কারণ অনেক সমস্যার বেসিক এখান থেকেই শুরু হয়।

উদাহরণ:  
Number = `1234`  
Digits = `4, 3, 2, 1` (ডান দিক থেকে)

---

### 🧠 Core Logic
Digit বের করার জন্য আমরা সাধারণত দুটি অপারেশন ব্যবহার করি:

- **Modulus (%)** → শেষ digit বের করতে  
- **Integer Division (//)** → শেষ digit বাদ দিতে  

## Formula:
- `digit = n % 10`
- `n = n // 10`

---

### 🧪 Example (Step by Step)

ধরা যাক,
```
n = 1025
```

| Step | n     | digit = n % 10 |
|-----|------|----------------|
| 1   | 1025 | 5              |
| 2   | 102  | 2              |
| 3   | 10   | 0              |
| 4   | 1    | 1              |

---

### 💻 Sample Code (Python)

```python
n = 1025

while n > 0:
    digit = n % 10
    print(digit)
    n = n // 10
```
### Output:
```
5
2
0
1
```

## ⚠️ Edge Cases
- যদি number = 0 হয় → আলাদা করে handle করতে হবে
- Negative number হলে → আগে abs(n) নিতে হবে

## 🔁 Common Problems Based on Digit Extraction
- Reverse a Number
- Palindrome Check
- Sum of Digits
- Count Digits
- Armstrong Number
- Digit Frequency

## 🎯 Why This Topic is Important?
- Loop logic strong হয়
- Number manipulation পরিষ্কার হয়

## বড় DSA problem solve করার foundation তৈরি হয়

## ✅ Summary
- Digit Extraction =
- ➡️ n % 10 → digit বের
- ➡️ n // 10 → number ছোট করা
- ➡️ Loop চলবে যতক্ষণ n > 0


