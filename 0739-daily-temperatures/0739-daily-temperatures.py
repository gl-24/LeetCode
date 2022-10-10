class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack,res = deque(),[]
        for i in range(len(temp)-1,-1,-1):
            while stack and temp[stack[-1]] <= temp[i]:
                stack.pop()
            if stack:
                res.append(stack[-1] - i)
            else:
                res.append(0)
            stack.append(i)
        return res[::-1]