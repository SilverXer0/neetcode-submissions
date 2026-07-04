class Solution:
    def isValid(self, s: str) -> bool:
        p = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []

        for i in range(len(s)):
            if s[i] in p:
                if stack and stack[-1] == p[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
            
        return len(stack) == 0