import sys
import heapq
sys.stdin = open('bj_14241.txt', 'r')

def heapsort(iterable): #오름차순 정렬
    h=[]
    for value in iterable:
        heapq.heappush(h,value)
    return [heapq.heappop(h) for _ in range(len(h))]


#### heapq로 한 것
n = int(input())
m = list(map(int, input().split()))
heapq.heapify(m)
a=[]
for i in range(n):
    a.append(-m[i]) #음수로 저장
heapq.heapify(a)
count = 0
for i in range(n-1):
    heapsort(a) #음수로 저장했기 때문에 내림차순 -> -10,-9,-8,-7 등등
    k1= -heapq.heappop(a)  #heappop()이 맨 앞 index를 반환 -> -10 * -1 = 10
    k2 = -heapq.heappop(a) # -9 * -1 = 9
    count = count+(k1 * k2)
    a.append(-(k1+k2))
print(count)


