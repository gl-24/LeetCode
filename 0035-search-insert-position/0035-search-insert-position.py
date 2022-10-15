class Solution:
    def searchInsert(self, arr: List[int], t: int) -> int:
        left, right = 0, len(arr)
        while left < right :
            mid = left + (right - left) // 2 
            if arr[mid] >= t:
                right = mid 
            else:
                left = mid + 1
        return left