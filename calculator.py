# ID 92126099

from operator import add, sub, mul, floordiv


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        try:
            return self.__items.pop()
        except IndexError:
            raise IndexError("Стек не содержит элементов")


def calculate(elements):
    stack = Stack()
    operator_functions = {
        '+': add, '-': sub,
        '*': mul, '/': floordiv
    }

    for element in elements:
        if element not in operator_functions:
            stack.push(int(element))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operator_functions[element](operand1, operand2)
            stack.push(result)

    return stack.pop()


if __name__ == '__main__':
    elements = input().split()
    print(calculate(elements))
