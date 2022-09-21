class Solution:
    def search(self, arr: List[int], t: int) -> int:
        lo = 0
        hi = len(arr) 
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] > t:
                hi = mid
            else:
                lo = mid + 1
        if arr[lo-1] != t:
            return -1 
        return lo - 1