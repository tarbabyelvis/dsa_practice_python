

def binary_search(arr: list[int], num: int) -> int:
    """
    search a number in a sorted array [1, 2, 3, 4,5] num=4
    returns index if found otherwise return -1
    """
    left,right = 0, len(arr) -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            right = mid -1 
        else:
            left  = mid + 1   
    return -1        
           
   

