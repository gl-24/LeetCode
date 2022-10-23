class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = end = 0
        d = 0
        mp = dict()
        while end < len(fruits):
            if fruits[end] not in mp:
                mp[fruits[end]] = 1
            else:
                mp[fruits[end]] += 1
            
            while len(mp) > 2:
                mp[fruits[start]] = mp.get(fruits[start],0) - 1
                if mp[fruits[start]] == 0:
                    mp.pop(fruits[start])
                start += 1
            d = max(d, end - start + 1)
            end += 1
        return d