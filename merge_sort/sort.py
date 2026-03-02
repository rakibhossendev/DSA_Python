from merge import merge_array

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge_array(left,right)
    
arr = [1,4,5,6,7,2,3]
x = merge_sort(arr)
print(x)