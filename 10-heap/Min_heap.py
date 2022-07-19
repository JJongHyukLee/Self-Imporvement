class heap:
    def __init__(self, data_list=None):
        self.heap_array = [0]
        if data_list is not None:
            self.heap_array.extend(data_list)

        for i in range(self.size() // 2, 0, -1):  # 부모 노드 기준으로 heapify 진행
            self.heapify(i)

    def size(self):
        return len(self.heap_array) - 1

    def heapify(self, parent_number):
        left_child = parent_number * 2
        right_child = parent_number * 2 + 1

        Min = parent_number  # min heap 이론상 parent가 Min ) root는 제일 작음.

        if left_child <= self.size() and self.heap_array[left_child] < self.heap_array[Min]:
            Min = left_child
        if right_child <= self.size() and self.heap_array[right_child] < self.heap_array[Min]:
            Min = right_child

        if Min != parent_number:
            self.heap_array[Min], self.heap_array[parent_number] = self.heap_array[parent_number], self.heap_array[Min]
            self.heapify(Min)  # 재귀함수를 통해 전체 tree로 보았을 때 모두 제 자리에 가있는지 확인.

    def heap_sort(self):  # Max heap = 내림차순
        # Max_heap을 오름차순으로 만들어 주는 것
        # Min_heap : 오름차순

        save = self.heap_array[:]
        sorted_list = self.heap_array[1:]

        for i in range(self.size(), 0, -1):
            self.heap_array[1], self.heap_array[i] = self.heap_array[i], self.heap_array[1]
            sorted_list[i - 1] = self.heap_array[i]
            self.heap_array.pop()
            self.heapify(1)
        self.heap_array = save
        return sorted_list

    def pop(self):
        if self.size() == 0:
            return None
        item = self.heap_array[1]
        self.heap_array[1] = self.heap_array[self.size()]
        self.heap_array.pop()
        self.heapify(1)

        return item

#    def insert(self, data):
 #       self.heap_array.append(data)
       # self.heapify(data)
       #이렇게 해도 프로그램은 작동하지만 data != parent_number 이므로 부적절해보임
       # 실제로 200을 넣으니 안됨.


    def insert(self, data):
        self.heap_array.append(data)
        k = self.size()
        while k > 1 and self.heap_array[k] < self.heap_array[k // 2]:
            self.heap_array[k], self.heap_array[k // 2] = self.heap_array[k // 2], self.heap_array[k]
            k // 2


import random
import time

start = time.time()
#x = random.sample(range(10),10) #w중복 x 범위, 총개수
x= [1,9,2,100,22]
h = heap(x)

h.insert(200)
h.insert(25)
h.insert(33)
h.insert(44)
h.insert(424)
h.sort()
print(h.heap_array)

for i in range(len(x)+1):
    print(h.pop())
print("걸린시간 : ",time.time()-start)




