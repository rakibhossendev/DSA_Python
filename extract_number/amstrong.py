n = 153
num = n # num = 153
len_num = len(str(n)) # len_num = 3
total = 0

while num > 0: # 153 > 0: | 15 > 0: | 1 > 0: | 0 > 0: False
    last_digits = num % 10 # last_digits = 3 | last_digit = 5 | last_digits = 1
    total += (last_digits ** len_num) # 27 | 125 + 27 = 152 | 152 + 1 = 153
    num //= 10 # 15 | 1 | 0
    
if total == n:
    print(n,"is amstrong number")
else:
    print(n,"is not amstrong number")