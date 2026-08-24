class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        temp_stack = { ")" : "(", "]" : "[", "}" : "{" }

        for i in s: 
            if i in temp_stack:
                if stack and stack[-1] == temp_stack[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
            
