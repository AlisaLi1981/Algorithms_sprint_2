# ID 92099471

from operator import add, sub, mul, floordiv


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.__items.pop()
        else:
            raise IndexError("Стек не содержит элементов")

    def is_empty(self):
        return len(self.__items) == 0


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
