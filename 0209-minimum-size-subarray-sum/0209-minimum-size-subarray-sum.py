class Solution:
    def minSubArrayLen(self, t: int, arr: List[int]) -> int:
        start = end = 0
        d = len(arr) + 1
        size = len(arr)
        add = 0
        while end < size:
            add += arr[end]
            while add >= t:
                d = min(d,end - start + 1)
                add -= arr[start]
                start += 1
            
            end += 1
        return d if d != len(arr)+1 else 0