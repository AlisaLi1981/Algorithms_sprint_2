# ID 92119092

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
            raise DequeFullError('error')
        self.__data[self.__tail] = value
        self.__tail = self.__calculate_index(self.__tail + 1)
        self.__size += 1

    def push_front(self, value):
        if self.__size >= self.__max_size:
            raise DequeFullError('error')
        self.__head = self.__calculate_index(self.__head - 1)
        self.__data[self.__head] = value
        self.__size += 1

    def pop_front(self):
        if self.__size <= 0:
            raise DequeEmptyError('error')
        value = self.__data[self.__head]
        self.__head = self.__calculate_index(self.__head + 1)
        self.__size -= 1
        return value

    def pop_back(self):
        if self.__size <= 0:
            raise DequeEmptyError('error')
        value = self.__data[self.__tail - 1]
        self.__tail = self.__calculate_index(self.__tail - 1)
        self.__size -= 1
        return value


def process_commands(deque):
    results = []
    for _ in range(number_of_commands):
        try:
            command, *params = input().split()
            result = getattr(deque, command)(*params)
            if 'pop' in command:
                results.append(result)
        except DequeFullError:
            results.append('error')
        except DequeEmptyError:
            results.append('error')
    return results


if __name__ == '__main__':
    number_of_commands = int(input())
    max_size = int(input())
    deque = Deque(max_size)
    results = process_commands(deque)
    for result in results:
        print(result)
