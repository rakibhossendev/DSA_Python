def func(i,N):
    if i > 5:
        return
    print(i)
    func(i+1,N)
    
func(1,4)    
    
        