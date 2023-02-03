class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        stack = []
        for par in s:
            if par in opening:
                stack.append(par)
            elif par in closing:
                if stack:
                    top = stack[-1]
                    index = opening.index(top)
                    if closing[index] == par:
                        stack.pop()
                        continue
                return False
        if stack:
            return False
        return True

                    