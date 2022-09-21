class Solution:
    def searchRange(self, arr: List[int], t: int) -> List[int]:
        def search(x):
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (hi + lo) >> 1
                if arr[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid 
            return lo
        
        first = search(t)
        last = search(t+1)-1
        if first <= last:
            return [first, last]
        return [-1,-1]