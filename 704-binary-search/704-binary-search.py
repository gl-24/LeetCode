class Solution:
    def search(self, nums: List[int], t: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == t:
                return mid
            elif nums[mid] > t:
                end = mid-1
            else:
                start = mid + 1
        return -1