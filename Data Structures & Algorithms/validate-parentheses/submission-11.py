class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for i in range(len(s)):
            if s[i] in d:
                if stack and stack[-1] == d[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
            

        return len(stack) == 0
