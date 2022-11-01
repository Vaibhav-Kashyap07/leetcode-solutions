class Solution:
    def isValid(self, s: str) -> bool:
        Map = {"}":"{", "]":"[", ")":"("}
        stack = []
        for c in s:
            if c in Map:
                if stack and Map[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack