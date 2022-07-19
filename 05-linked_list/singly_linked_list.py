class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None #뒤의 시작 node를 가리키게 하여 이어지게 할 수 있음.

#__init__함수 : constructure 함수 -> node class가 object가 되면 제일 먼저 실행되는 함수

class SinglyLinkedList:
    def __init__(self):
        self.head = None #head라는 reference varialble은 첫 node 주소의 시작 주소를 가리키는 reference variable
        self.size = 0

    def insert(self,prev_node, data): #prev_node : 앞 node의 reference variable
        node = Node(data)
        self.size += 1
        if prev_node:
            node.next = prev_node.next
            prev_node.next = node
            #insert as the head node (empty or not)
        else:
            node.next = self.head
            self.head = node


    def traverse(self):
        current = self.head
        while current:
            yield current.data
            current = current.next


    def delete(self,prev_node):
        self.size -= 1

        #delete a non head node
        if prev_node:
            prev_node.next = prev_node,next.next
        #delete the head node
        else:
            self.head - self.head.next


word = SinglyLinkedList()
word.insert(None,"eggs")
word.insert(word.head.next,"ham")
word.insert(word.head,"toast")
word.insert(word.head,"sejun")

for s in word.traverse():
    print(s)


