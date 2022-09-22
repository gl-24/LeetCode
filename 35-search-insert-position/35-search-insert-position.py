class Solution:
    def searchInsert(self, arr: List[int], t: int) -> int:
        lo,hi = 0,len(arr)
        while lo < hi:
            mid = (lo + hi) >> 1
            if arr[mid] >= t:
                hi = mid 
            else :
                lo = mid + 1
        return lo