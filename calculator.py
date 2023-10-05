# ID 92078053

class Calculator:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):    
        return self.items.pop()    


def calculate(elements):
    stack = Calculator()
    operators = {'+', '-', '*', '/'}

    for element in elements:
        if element not in operators:
            stack.push(int(element))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if element == '+':
                stack.push(operand1 + operand2)
            elif element == '-':
                stack.push(operand1 - operand2)
            elif element == '*':
                stack.push(operand1 * operand2)
            elif element == '/':
                stack.push(operand1 // operand2)

    return stack.pop()


elements = input().split()

print(calculate(elements))
