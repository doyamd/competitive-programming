class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i != "+" and i != "-" and i != "*" and i != "/":
                stack.append(int(i))
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if i == "+":
                    stack.append(num1+num2)
                elif i == "-":
                    stack.append(num1 - num2)
                elif i == "*":
                    stack.append(num1 * num2)
                elif i == "/":
                    stack.append(int(num1/num2))
        return stack[-1]
                