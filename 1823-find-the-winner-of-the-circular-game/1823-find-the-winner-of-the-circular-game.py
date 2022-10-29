class Solution:
    def solve(self,arr,index,k):
        if len(arr) == 1:
            return arr[0]
        index = (index + k) % len(arr)
        arr.pop(index)
        self.solve(arr,index,k)
        return arr[0]
        
    def findTheWinner(self, n: int, k: int) -> int:
        arr = list(range(1,n+1))
        index = 0
        last_man = self.solve(arr,index,k-1)
        return last_man