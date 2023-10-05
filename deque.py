# ID 91841749

from typing import List, Optional


class CircularDeque:
    def __init__(self, max_size):
        self.max_size = max_size
        self.data: List[Optional[int]] = [None] * max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def push_back(self, value):
        if self.size < self.max_size:
            self.data[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            return 'error'

    def push_front(self, value):
        if self.size < self.max_size:
            self.head = (self.head - 1) % self.max_size
            self.data[self.head] = value
            self.size += 1
        else:
            return 'error'

    def pop_front(self):
        if self.size > 0:
            value = self.data[self.head]
            self.head = (self.head + 1) % self.max_size
            self.size -= 1
            return value
        else:
            return 'error'

    def pop_back(self):
        if self.size > 0:
            value = self.data[self.tail - 1]
            self.tail = (self.tail - 1) % self.max_size
            self.size -= 1
            return value
        else:
            return 'error'

n = int(input())
m = int(input())
deque = CircularDeque(m)

for _ in range(n):
    command = input().split()
    if command[0] == 'push_back':
        _, value = command
        result = deque.push_back(int(value))
        if result == 'error':
            print("error")
    elif command[0] == 'push_front':
        _, value = command
        result = deque.push_front(int(value))
        if result == 'error':
            print('error')
    elif command[0] == 'pop_front':
        result = deque.pop_front()
        if result == 'error':
            print('error')
        else:
            print(result)
    elif command[0] == 'pop_back':
        result = deque.pop_back()
        if result == 'error':
            print('error')
        else:
            print(result)
