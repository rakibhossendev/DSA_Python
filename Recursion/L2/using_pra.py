def func(x,n):
    if n == 0:
        return
        
    print(x)
    func(x,n-1)
    
func(16,4)    