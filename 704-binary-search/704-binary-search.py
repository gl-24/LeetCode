class Solution:
    def search(self, arr: List[int], t: int) -> int:
        lo,hi= 0,len(arr)
        while lo < hi:
            mid = (lo +hi) >>1
            if arr[mid] >= t:
                hi = mid
            else:
                lo = mid + 1
        if arr[lo%len(arr)] != t:
            return -1
        return lo