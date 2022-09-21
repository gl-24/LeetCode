class Solution:
    def findMin(self, arr: List[int]) -> int:
        n = len(arr)
        start = 0 
        end = n - 1
        if n == 1:
            return arr[0]
        while start <= end:
            mid = start + (end - start) // 2 
            pre = (mid - 1 + n) % n
            nex = (mid + 1) % n
            
            if arr[mid] < arr[pre]:
                return arr[mid]
            if arr[mid] > arr[nex]:
                return arr[nex]
            if arr[mid] > arr[0]:
                start = mid + 1
            else:
                end = mid - 1
        return -1