nums = [1,3,2,5,7,8,9,4]
for i in range(1,len(nums)):
    key = nums[i]
    j = i - 1
    while j >= 0 and nums[j] > key:
        nums[j+1] = nums[j]
        
    nums[j+1] = key        