class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        left, right = 0,0

        for token in tokens:
            if token == "+":
                right,left = stack.pop(),stack.pop()
                stack.append(left+right)
            elif token == "-":
                right,left = stack.pop(),stack.pop()
                stack.append(left-right)
            elif token == "*":
                right,left = stack.pop(),stack.pop()
                stack.append(left*right)
            elif token == "/":
                right,left = stack.pop(),stack.pop()
                stack.append(int(left/right))
            else:
                stack.append(int(token))

        return stack[0]