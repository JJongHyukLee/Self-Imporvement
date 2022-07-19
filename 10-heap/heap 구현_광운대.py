class maxheap:
    def __init__(self,data_list=None):
        self.heap_array = [None]
        if data_list is not None:
            self.heap_array.extend(data_list)
        for i in range(self.size()//2, 0, -1): # for loop를 internal 노드에서만
                                               # leaf노드가 달려 있는 가장 마지막 부모 노드부터 root 노드까지
            self.max_heapify(i)

    def size(self):
        return len(self.heap_array) -1

    def max_heapify(self,parent_number):
        left_child = parent_number * 2
        right_child = parent_number *2 +1

        largest = parent_number

        if left_child <= self.size() and self.heap_array[left_child] > self.heap_array[largest]:
            largest = left_child
        if right_child <= self.size() and self.heap_array[right_child] > self.heap_array[largest]:
            largest = right_child

        if largest != parent_number:
            self.heap_array[parent_number], self.heap_array[largest] = self.heap_array[largest], self.heap_array[parent_number]
            self.max_heapify(largest)

    def heap_sort(self):
        save = self.heap_array[:] # heap_array를 sallow copy
        sorted_list = self.h[1:] # heap_array를 index 1번부터 sallow copy
        for i in range(self.size(), 0 , -1):
            self.heap_array[1], self.heap_array[i] = self.heap_array[i], self.heap_array[1]
            sorted_list[i-1] = self.h[i]
            self.heap_array.pop()
            self.max_heapify(1)
        self.heap_array = save
        return sorted_list

    def pop(self):
        if self.size == 0:
            return None

        max = self.heap_array[1]
        self.heap_array[1] = self.heap_array[self.size()]
        self.heap_array.pop()
        self.max_heapify(1)

        return max
    def insert(self,data):
        self.heap_array.append(data)

        k = self.size()

        while k>1 and self.heap_array[k] > self.h[k//2]:
            self.heap_array[k], self.heap_array[k//2] = self.h[k//2],self.h[k]
            k//=2

x= [1,5,6,7,8,3,2,4]
h = maxheap(x)
print(h.heap_array)