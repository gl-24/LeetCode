class Solution:
    def bs(self,arr, startIndex, endIndex, x):
        lo, hi = startIndex, endIndex
        while lo < hi :
            mid = (lo + hi) >> 1
            if arr[mid] >= x:
                hi = mid
            else:
                lo = mid + 1
        if(arr[lo%len(arr)] != x):
            return -1
        return lo
    
    def indexOfMinEle(self, arr):
        lo, hi = 0, len(arr)-1
        while lo < hi:
            mid = (lo + hi) >> 1
            if arr[mid] < arr[hi]:
                hi = mid
            else:
                lo = mid + 1
        return lo
    
    
    def search(self, nums: List[int], t: int) -> int:
        if len(nums)==1 and nums[0] == t:
            return 0
        index = self.indexOfMinEle(nums)
        ind1 = self.bs(nums,0,index,t)
        ind2 = self.bs(nums,index,len(nums),t)
        if ind1 != -1:
            return ind1
        elif ind2 != -1:
            return ind2
        else:
            return -1