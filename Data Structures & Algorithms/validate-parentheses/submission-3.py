class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")" : "(", "}" : "{", "]" : "["}

        for i in range(len(s)):
            if s[i] in pairs:
                if len(stack) != 0 and stack[-1] == pairs[s[i]]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(s[i])

        if len(stack) == 0:
            return True
        else:
            return False