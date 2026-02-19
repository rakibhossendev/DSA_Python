'''def func(sum,i,n):
    if sum == n:
        return
    sum += i
    print(sum)
    func(sum,i+1,n)
    
func(0,1,55)    
'''

def func(sum,i,n):
    if i > n:
        print(sum)
        return
    func(sum+i,i+1,n)
    
func(0,1,10)    
        