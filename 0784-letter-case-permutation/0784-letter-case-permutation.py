class Solution:
    def solve(self,ip,op,l):
        if len(ip) == 0:
            l.append(op)
            return 
        op1 = op2 = op
        op1 += ip[0].upper()
        op2 += ip[0].lower()
        ip = ip[1:]
        self.solve(ip,op1,l)
        self.solve(ip,op2,l)
        return l
        
    def letterCasePermutation(self, s: str) -> List[str]:
        ip = s
        op = ""
        lst = []
        l = self.solve(ip,op,lst)
        mp = {}
        for i in l:
            if i not in mp:
                mp[i] = 1
        return mp.keys()