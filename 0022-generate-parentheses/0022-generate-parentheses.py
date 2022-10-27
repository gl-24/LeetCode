class Solution:
    def solve(self,open,close,op,l):
        if open == 0 and close == 0:
            l.append(op)
            return 
        if open != 0:
            op1 = op 
            op1 += "("
            self.solve(open-1,close,op1,l)
        
        if close > open:
            op2 = op 
            op2 += ")"
            self.solve(open,close-1,op2,l)
            
        return l
    def generateParenthesis(self, n: int) -> List[str]:
        open = close = n 
        l = []
        op = ""
        ans = self.solve(open,close,op,l)
        return ans