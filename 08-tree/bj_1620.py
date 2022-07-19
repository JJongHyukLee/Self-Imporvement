import sys
sys.stdin = open('bj_1620.txt')

class Node:
    def __init__(self,data=None,num=None):
        self.data = data
        self.num = num
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
    def find_min(self):
        node = self.root
        while node.left:
            node = node.left
        return node
    def find_max(self):
        node = self.root
        while node.right:
            node = node.right
        return node

    def insert(self, data, num):

        node = Node(data,num)
        parent = None
        current = self.root

        while current:
            parent = current
            if node.data < current.data:
                current = current.left
            else:
                current = current.right
        if parent is None:
            self.root = node
        elif node.data < parent.data:
            parent.left = node
        else:
            parent.right = node

    def search(self,data):
        node = self.root
        while True:
            if node is None:
                return node
            elif node.data == data:
                return node.num
            elif data<node.data:
                node = node.left
            else:
                node = node.right
n,m = map(int,input().split())
name_list = []
tree = Tree()

for i in range(1,n+1):
    name = sys.stdin.readline().rstrip('\n')
    name_list.append(name) #이름 저장
    tree.insert(name,i) #이름과 순서 저장
    #print(tree.search(i))

for i in range(m):
    qury_ = sys.stdin.readline().rstrip('\n')
    if qury_[0].isalpha(): #qury는 string이기 때문에 index로 영문자 확인
        print(tree.search(qury_)) #영문자라면 영문자를 tree에 search로 넘겨주어 data(번호)반환
    else:
        qury_ = int(qury_) #영문자가 아니라면 스트링을 int로 바꾼 후
        print(name_list[qury_-1]) # 이름 출력
