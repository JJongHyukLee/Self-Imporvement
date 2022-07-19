#import sys
#sys.stdin = open('bj9012_in.txt', 'r')


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)

        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None

        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        if self.size == 0:
            return None
        return self.top.data


tc = int(input())

for _ in range(tc):
    s = Stack()
    test = input()
    for c in test:
        if c in '(':
            s.push(c)
        if c in ')':
            last = s.pop()
            if last == '(' and c == ')':
                continue
            elif last is None:
                break

    if s.size > 0 or last is None:
        print('NO')
    else:
        print('YES')

