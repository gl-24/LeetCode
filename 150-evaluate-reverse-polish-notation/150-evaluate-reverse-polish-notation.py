class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operators = "+-*/"
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                num1,num2 = stack.pop(),stack.pop()
                if token == "+":
                    stack.append(num2+num1)
                elif token == "-":
                    stack.append(num2-num1) 
                elif token == "*":
                    stack.append(num2*num1) 
                else:
                    stack.append(int(num2/num1))
        return stack.pop()