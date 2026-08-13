class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i in "+-*/":
                num1 = stack.pop()
                num2 = stack.pop()

                if i == "+":
                    num = num2 + num1
                elif i == "-":
                    num = num2 - num1
                elif i == "*":
                    num = num2 * num1
                else:
                    num = int(num2/num1)

                stack.append(num)
            
            else:
                stack.append(int(i))
        
        return stack[-1]