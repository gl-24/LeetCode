class Solution:
    def bs(self,arr, t , left, right):
        while left < right:
            mid = left + (right - left) // 2 
            if arr[mid] >= t:
                right = mid 
            else:
                left = mid + 1
        if arr[left % len(arr)] != t:
            return -1
        return left
    
    def min_element(self,arr):
        left, right = 0, len(arr) - 1 
        while left < right:
            mid  = left + (right - left) // 2
            if arr[mid] < arr[right]:
                right = mid 
            else:
                left = mid+1
        return left 
    
    def search(self, arr: List[int], t: int) -> int:
        if len(arr)==1 and arr[0] == t:
            return 0
        pos = self.min_element(arr)
        ind1 = self.bs(arr,t, 0,pos)
        ind2 = self.bs(arr,t, pos, len(arr))
        if ind1 != -1:
            return ind1 
        elif ind2 != -1:
            return ind2 
        else:
            return -1 
        
        


