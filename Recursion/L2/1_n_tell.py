def func(i,N):
    if i < 1:
        return
    func(i-1,N)
    print(i)
    
func(4,1)    
    
        