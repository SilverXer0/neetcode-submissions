class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = set(["+", "-", "*", "/"])
        stack = []

        for token in tokens:
            if token in operations:
                v1 = stack.pop()
                v2 = stack.pop()
                if token == "+":
                    stack.append(v1 + v2)
                elif token == "-":
                    stack.append(v2 - v1)
                elif token == "*":
                    stack.append(v1 * v2)
                else:
                    stack.append(int(float(v2) / v1))
            else:
                stack.append(int(token))

        return stack[-1]
