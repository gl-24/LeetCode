class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = deque()
        res = []
        for i in range(len(temp)-1,-1,-1):
            if not stack:
                res.append(0)
            elif temp[stack[-1]] > temp[i]:
                res.append(stack[-1]-i)
            else:
                while stack and temp[stack[-1]] <= temp[i]:
                    stack.pop()
                if stack and temp[stack[-1]] > temp[i]:
                    res.append(stack[-1]-i)
                else:
                    res.append(0)
            stack.append(i)
        return res[::-1]