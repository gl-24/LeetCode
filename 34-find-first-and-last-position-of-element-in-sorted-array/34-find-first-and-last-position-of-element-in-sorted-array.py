class Solution:
    def firstOccurance(self,arr, t):
        start = 0
        end = len(arr) - 1
        res = -1
        while start <= end:
            mid = start + (end - start) // 2 
            if arr[mid] == t:
                res = mid 
                end = mid - 1
            elif arr[mid] < t:
                start = mid + 1
            else:
                end = mid - 1
        return res
    
    def lastOccurance(self,arr, t):
        start = 0
        end = len(arr) - 1
        res = -1
        while start <= end:
            mid = start + (end - start) // 2 
            if arr[mid] == t:
                res = mid 
                start = mid + 1
            elif arr[mid] < t:
                start = mid + 1
            else:
                end = mid - 1
        return res
    
    def searchRange(self, nums: List[int], t: int) -> List[int]:
        first = self.firstOccurance(nums,t)
        last = self.lastOccurance(nums,t)
        return [first, last]