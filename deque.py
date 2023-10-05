# ID 92130380

from typing import List, Optional


class DequeFullError(Exception):
    pass


class DequeEmptyError(Exception):
    pass


class Deque:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__data: List[Optional[int]] = [None] * max_size
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def __calculate_index(self, index):
        return index % self.__max_size

    def push_back(self, value):
        if self.__size >= self.__max_size:
            raise DequeFullError('Лимит элементов исчерпан!')
        self.__data[self.__tail] = value
        self.__tail = self.__calculate_index(self.__tail + 1)
        self.__size += 1

    def push_front(self, value):
        if self.__size >= self.__max_size:
            raise DequeFullError('Лимит элементов исчерпан!')
        self.__head = self.__calculate_index(self.__head - 1)
        self.__data[self.__head] = value
        self.__size += 1

    def pop_front(self):
        if self.__size <= 0:
            raise DequeEmptyError('Очередь пуста!')
        value = self.__data[self.__head]
        self.__head = self.__calculate_index(self.__head + 1)
        self.__size -= 1
        return value

    def pop_back(self):
        if self.__size <= 0:
            raise DequeEmptyError('Очередь пуста!')
        value = self.__data[self.__tail - 1]
        self.__tail = self.__calculate_index(self.__tail - 1)
        self.__size -= 1
        return value


def process_commands(deque, command):
    try:
        cmd, *params = command.split()
        return getattr(deque, cmd)(*params)
    except (DequeFullError, DequeEmptyError):
        return 'error'


if __name__ == '__main__':
    number_of_commands = int(input())
    max_size = int(input())
    deque = Deque(max_size)
    for _ in range(number_of_commands):
        command = input()
        result = process_commands(deque, command)
        if result is not None:
            print(result)
