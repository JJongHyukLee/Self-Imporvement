class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CircularList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, prev_node, data):
        node = Node(data)
        self.size += 1

        if prev_node:
            node.next = prev_node.next
            prev_node.next = node

        else:
            node.next = node
            self.head = node

    def traverse(self):
        current = self.head
        while True:
            yield current.data
            if current.next == self.head:
                break
            else:
                current = current.next

    def delete(self, prev_node):
        self.size -= 1

        if prev_node.next != self.head:
            prev_node.next = prev_node.next.next


        else:
            if prev_node != self.head:
                self.head = self.head.next
                prev_node.next = self.head

            else:
                self.head = None

#요세푸스
n, k = map(int, input().split())

jo = CircularList()

jo.insert(None,1)
answer= []
b=[]
q = 0
'''
for jo in jo.traverse():
    print(jo)
'''
for i in range(n, 1, -1):  # 1->2->3->4->5->6->7->1 circuit 구현

    jo.insert(jo.head, i)

for i in range(n):
    if k != 1:
        if q == 0:
            jo.head = jo.head.next

        else:
            for a in range(k-1):
                jo.head = jo.head.next

        answer.append(jo.head.next.data)
        jo.delete(jo.head)
        q = q+1
    else :
        answer.append(jo.head.data)
        jo.head=jo.head.next



print('<', end='')
for i in range(n):
    if (i != n -1):
        print(f'{answer[i]}, ', end="")
    else:
        print(f'{answer[i]}', end="")
print('>', end="")