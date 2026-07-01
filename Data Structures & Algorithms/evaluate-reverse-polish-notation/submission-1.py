class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                value1, value2 = stack.pop(), stack.pop()
                stack.append(value2 - value1)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                value1, value2 = stack.pop(), stack.pop()
                stack.append(int(float(value2 / value1)))
            else:
                stack.append(int(token))

        return stack.pop()