"""Write a function that finds the maximum element in each sliding window 
of size k in an array. Return a list of maximums for each window position.

The function should:
- Slide a window of size k through the array
- Find the maximum element in each window position
- Return a list of maximum values
- Handle edge cases (empty array, k <= 0, k > array length)
- Return empty list for invalid inputs
Function signature"""
def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    
    result = []
    if len(nums) == 0:
        return result
    if k <= 0:
        return result
    if len(nums) < k:
        return result
    
    for ind in range(len(nums)-k+1):
        result.append(max(nums[ind:ind+k]))

    return result
    



print(sliding_window_maximum([1,3,-1,-3,5,3,6,7], 3))