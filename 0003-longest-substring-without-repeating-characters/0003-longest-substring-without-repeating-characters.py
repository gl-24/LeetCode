class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = end = 0
        mp = dict()
        d = 0
        while end < len(s):
            ch = s[end]
            mp[ch] = mp.get(ch,0)+1
            while mp[ch] > 1:
                mp[s[start]] -= 1
                start += 1
            d = max(d, end - start + 1)
            end += 1
        return d
    