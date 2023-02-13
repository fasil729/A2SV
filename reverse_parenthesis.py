class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ")":
                stack.append(char)
            else:
                buffer = ""
                while stack[-1] != "(":
                    buffer += stack.pop()
                stack.pop()

                stack.extend(buffer)
        return "".join(stack)