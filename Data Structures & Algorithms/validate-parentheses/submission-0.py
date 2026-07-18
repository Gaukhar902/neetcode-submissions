class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in s:
            if i in "([{":
                stack.append(i)

            if i in ")]}":
                if not stack:
                    return False

                if stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0