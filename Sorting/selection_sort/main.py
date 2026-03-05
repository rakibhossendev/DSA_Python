def selectionSorting(nums):
    n = len(nums) # n = 9
    for i in range(0, n): # range(0,9)
        min_index = i # min_index = 0 
        for j in range(i+1, n): # range(1,9)
            if nums[j] < nums[min_index]:  # if nums[0] < nums[0]
                min_index = j # min_index = 1
        nums[i], nums[min_index] = nums[min_index], nums[i] # nums[0],nums[0]
    return nums  
    
#       0  1 2 3 4 5 6 7 8 9
nums = [10,7,6,5,8,9,3,2,1,4]
#        
sorted_l = selectionSorting(nums)
print(sorted_l)