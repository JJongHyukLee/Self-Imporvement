import sys
import heapq
sys.stdin = open('bj_14235.txt', 'r')

def heapsort(iterable): #오름차순
    h=[]
    for value in iterable:
        heapq.heappush(h,value)
    return [heapq.heappop(h) for _ in range(len(h))]
#### heapq로 한 것
n = int(input())
a=[]
for _ in range(n):
    m = list(map(int,input().split()))

    if m[0] == 0:
        if len(heapsort(a)) == 0: # 0 =flase =none 거짓의 의미.
                                  # heapsort는 원소들이 정렬된 list를 반환하기 떄문
            print(-1)
        else:
           k = heapq.heappop(a) #맨 앞의 것을 반환
           k = -k               # 음수로 저장했기에 문제 조건의 가장 큰 값이 나옴 -> 다시 -로...
           print(k)
    else:
        for i in range(m[0]):
            a.append(-m[i+1]) #음수로 저장
            heapq.heapify(a)
            heapsort(a) #저장을 음수로 -10 -9 -8 -7 -6.....

