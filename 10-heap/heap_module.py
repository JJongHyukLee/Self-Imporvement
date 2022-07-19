import heapq

def heapsort(iterable):
    h=[]
    for value in iterable:
        heapq.heappush(h,value)
        print(h)
    return [heapq.heappop(h) for _ in range(len(h))]

a = [3, 5, 1, 2, 6, 8, 7]

heapq.heapify(a)
print(a)

heapsort(a)
'''

b=[]
heapq.heappush(b, (5, 'write code'))
heapq.heappush(b, (7, 'release product'))
heapq.heappush(b, (1, 'write spec'))
print(heapq.heappop(b))
print(b)


f = [1,5,6,7,2,3,4,51,5,100]
for value in range(f):
    heapq.heappush(f,value)
print(f)
'''