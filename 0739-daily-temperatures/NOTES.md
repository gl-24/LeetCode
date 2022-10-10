*Bruteforce Approach*
```
class Solution:
def dailyTemperatures(self, temp: List[int]) -> List[int]:
res = [0]*len(temp)
for i in range(len(temp)-1):
for j in range(i+1,len(temp)):
if temp[i] < temp[j]:
res[i] = j-i
break
return res
```
Time Complexity : O(n^2)
​