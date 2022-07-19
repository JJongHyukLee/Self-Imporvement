import sys
sys.stdin = open('bj_14235.txt', 'r')

class MaxHeap:
    def __init__(self,data_list=None):
        self.h = [0]
        if data_list is not None:
            data_list
            self.h.extend(data_list)

        for i in range(self.size() //2,0,-1):
            self.max_heapify(i)

    def size(self):
        return len(self.h)-1

    def max_heapify(self,k):
        left = k*2
        right = k *2 +1

        largest = k
        if left <= self.size() and self.h[left]>self.h[largest]:
            largest = left
        if right <= self.size() and self.h[right] > self.h[largest]:
            largest = right

        if largest !=k:
            self.h[k],self.h[largest] = self.h[largest], self.h[k]
            self.max_heapify(largest)

    def heap_sort(self):
        save = self.h[:]
        sorted_list = self.h[1:]

        for i in range(self.size(),0,-1):
            self.h[1], self.h[i] = self.h[i],self.h[1]
            sorted_list[i-1]=self.h[i]
            self.h.pop()
            self.max_heapify(1)
        self.h = save
        return sorted_list

    def pop(self):
        if self.size() == 0:
            return None

        item = self.h[1]
        self.h[1] = self.h[self.size()]
        self.h.pop()
        self.max_heapify(1)
        return item

    def insert(self, item):
        self.h.append(item)
        k=self.size()
        while k>1 and self.h[k] > self.h[k//2]:
            self.h[k], self.h[k//2] = self.h[k//2], self.h[k]
            k //=2
n = int(input())
m=[]
h1 = MaxHeap(m) #10 9 8 7 6 5...순으로 ..
##### 원래 예제대로 한 것
for _ in range(n):
    m = list(map(int,input().split()))

    if m[0] == 0:
        o = h1.pop()#실행하자마자는 1 9 8 7 6 5 4 3 2 10이지만
                    #함수가 끝나면 9 8 7 6 5 4 3 2 1이 되어있음.
        if o is None:
            print(-1)

        else:
            print(o) #pop을 했는데 item이 있어 none으로 반환되지 않은 경우

    else:
        for i in range(m[0]):
            h1.insert(m[i+1]) #insert

