class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0

        for token in tokens:
            if token in '+-*/':
                num2 = stack.pop()
                num1 = stack.pop()

                if token == '+':
                    result = num1 + num2
                elif token == '-':
                    result = num1 - num2
                elif token == '*':
                    result = num1 * num2
                else:
                    result = int(num1 / num2)
                
                stack.append(result)
            
            else:
                stack.append(int(token))
        
        return stack[0]


        

        