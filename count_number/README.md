📌 Count Number (Digit Count) in Python

এই README তে আমরা শিখবো কীভাবে একটি সংখ্যার মোট কয়টি digit আছে তা বের করতে হয়। এটাকেই বলা হয় Count Number / Digit Count।

এখানে থাকবে 👇

✅ Problem Explanation

✅ Algorithm (Step by Step)

✅ Python Code

✅ Example & Output

✅ Alternative Method

✅ Notes



---

🔍 Problem Explanation

ধরা যাক আমাদের কাছে একটি সংখ্যা আছে:

15327

আমরা জানতে চাই—এই সংখ্যাটিতে মোট কয়টি digit আছে?

👉 Output হবে:

5

এই সমস্যাটি সাধারণত while loop এবং integer division ব্যবহার করে সমাধান করা হয়।


---

🧠 Algorithm (Digit Count)

Input: একটি পূর্ণসংখ্যা n

Output: digit এর মোট সংখ্যা count

📑 Steps:

1. Start


2. একটি সংখ্যা n নাও


3. count = 0 সেট করো


4. যতক্ষণ n > 0

n = n // 10

count = count + 1



5. count প্রিন্ট করো


6. End




---

🧾 Python Code (While Loop ব্যবহার করে)

n = int(input("Enter a number: "))
count = 0

while n > 0:
    n = n // 10
    count += 1

print("Total digits:", count)


---

▶️ Example Run

Input:

70984

Output:

Total digits: 5


---

⚠️ Special Case: Zero (0)

যদি input হয় 0, তাহলে while loop চলবে না। কিন্তু বাস্তবে 0-এর digit count = 1।

✔️ Correct Code with Zero Handling

n = int(input("Enter a number: "))

if n == 0:
    print("Total digits: 1")
else:
    count = 0
    while n > 0:
        n //= 10
        count += 1
    print("Total digits:", count)


---

🔄 Alternative Method (String ব্যবহার করে)

n = input("Enter a number: ")
print("Total digits:", len(n))

📝 Note: এই method সহজ, কিন্তু এটি loop ও number logic শেখার জন্য ভালো না।


---

📌 Key Notes

// 10 → প্রতি step এ একটি digit বাদ দেয়

Loop যতবার চলে = digit সংখ্যা

Interview ও basic problem solving এ খুব common



---

🎯 Where It’s Used?

Digit validation

Armstrong number check

Number length comparison

Data validation



---

✅ Conclusion

Count Number problem Python শেখার সময় একটি must-practice topic। এটি loop, integer division, এবং logical thinking clear করে।

Happy Coding 🚀