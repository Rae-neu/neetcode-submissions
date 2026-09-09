class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '[' or char == '(' or char == '{':
                stack.append(char)
            
            elif char == ']':
                if not stack or stack.pop() != '[':
                    return False
            
            elif char == ')':
                if not stack or stack.pop() != '(':
                    return False
            
            else:
                if not stack or stack.pop() != '{':
                    return False
        
        if stack:
            return False

        return True