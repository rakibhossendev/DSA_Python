n = int(input("Enter a digits: "))
digits = []
while n > 0:
    digits.append(n%10)
    
    n //= 10
    
[print(d) for d in reversed(digits)]  