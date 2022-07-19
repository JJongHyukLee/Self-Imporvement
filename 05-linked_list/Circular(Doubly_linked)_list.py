class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CircularList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, prev_node, data):
        node = Node(data) #data를 저장시키기 위한 Node object 생성
        self.size += 1 #list에 요소가 추가 됐기 때문

        #list is not empty
        if prev_node:
            node.next = prev_node.next
            prev_node.next = node
        #list is empty
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
n, k = map(int, input().split())

jo = CircularList()
if n != 0:
    jo.insert(None, 1)
for i in range(n, 1, -1):
    jo.insert(jo.head, i)

L = []
x = jo.head
count = 0

print('<', end='')

while jo.size != 1:   #circular list의 size가 2개 이상인 경우
    if k > 1:         #n번 째 사람을 뽑아야 하니 whlile문에서 size가 2이상이 ㄴ경우라 하여 k도 2이상인 경우여야함
        for i in range(k - 1): # 이미 1이 들어가 있으니, k-1번 loop
            count += 1         #0 1 2 3
            if count == k - 1: #count == 3
                continue
            x = x.next
        print(x.next.data, end=', ')
        jo.delete(x)
        count = -1 # count 초기화 맨 처음 돌 때는 2번 그다음엔 3번을 돌아야 함 -> 윗 코드는 1번만 옮김
                   # -> count = -1로 하여 1번 도는 코드를 2번 도는 코드로 변경
                   # 이미 head 자체가 1번을 가리키기 때문
                   # 첫 loop만 예외처리한 것임.
    else:
        if jo.size == n:
            for _ in range(n - 1):
                x = x.next
        print(x.next.data, end=', ')
        jo.delete(x)
        if jo.size == 0:
            break

print(x.data, end='>')