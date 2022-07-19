import sys
import heapq

max_heap, min_heap = [], []
m = int(sys.stdin.readline())
#완전이진트리 중간값 구하는 이론:
       # 1. 최소 힙의 값들은 모두 최대 힙보다 크도록 한다.
       #2. 최대 힙의 크기가 최소 힙의 크기보다 1크거나 같도록 한다.
       #3. 값을 넣어준 후 최대 힙의 max와 최소 힙의 min을 비교해 최소 힙의 min보다 최대 힙의 max가
       #더 크다면 값을 교환한다.
       #max힙의 idx = 0가 중간값이 된다.

for i in range(m): #길이는 항상 1차이나던가 안나야함.
    n = int(sys.stdin.readline())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-n,n)) #max_heap
    else:
        heapq.heappush(min_heap, (n,n)) #min_heap

#heapq.heappush(heap,(-num,num))
    # heapq는 min_heap만 지원 -> 튜플에 우선순위를 줌으로써 max_heap으로 만듦
    #값을 불러올 땐 각 튜플에서 인덱스 1에 있는 값을 취함.

######### min_heap이 존재한다는 것  = 오른 자식이 있다는 것// 오른 자식이 없다면 비교할 필요 x
    if min_heap and max_heap[0][1] > min_heap[0][0]:
        # 만약 max_heap에 값이 들어갔는데 max_heap에 더 큰 값이 들어갔을 경우는 조건에 맞지 않음
        #max_heap에 원소가 있으면서 min_heap이 max_heap보다 값이 큰 경우우
        max_heap_max = heapq.heappop(max_heap)[1] # max_heap의 최대값 -> max_heap 중 가장 큰 값
                                                  # 사실 max_heap이라 보긴 애매함 그냥 큰 수라 하자.
        min_heap_min = heapq.heappop(min_heap)[0] # min_heap 중 가장 큰 값
                                                  #min_heap은 가장 작은 값이 앞에 있음.

        heapq.heappush(max_heap,(-min_heap_min, min_heap_min)) #max_heap은 항상 min_heap보다 값이 작아야함
        heapq.heappush(min_heap,(max_heap_max, max_heap_max)) #min_heap은 항상 max_heap보다 커야함.
    print(max_heap[0][1]) #아래와 같은 설명 때문에 [0][1]
#print(max_heap)
#print(max_heap[0][1]) tuple의 우선순위 때문에 -99 1 2 5 -> (-5,5),(-2,1),(-1,1),(99,-99)로 저장
    #max_heap의 마지막 요소가 항상 중간값임
    #min_heap의 최소값보다 max_heap의 마지막 요소가 큰 경우
    #min_heap의 가장 앞 요소와 max_heap 마지막 요소를 바꿔주면됨
    # 부모노드의 자식 노드 중 왼쪽, 오른 쪽 노드들 중 대 소를 가리면 본다고 보면 됨
    #ex) max_heap = left_child
    #ex) min_heap = right_child
    #ex) 완전 이진 트리는 항상 부모->왼쪽->오른쪽으로 트리를 채움

    ######## 중앙값 특성에 따라 어떤 그룹에서 가장 작은 수 ,가장 큰 수만 필요하다! -> 최대 힙, 최소 힙



'''
max_heap으로 저장한 이유

min_heap 모듈인 heapq 사용 시 최대 힙으로 바꾸면 max_heap으로 바꿔야 하기 때문

max_heap으로 바꿨을 때 tuple의 우선순위 때문에 ..

다만 문제 풀이 조건이 max_heap 원소 < min_heap 임! 쭈의!

이론

1. min_heap과 max_heap과의 크기 차이가 1이하이다 -> 중간값 정리 
= 완전이진트리 채우는 순서 : 부모 -> 왼 자식 -> 오른 자식

2. 만약 max_heap 원소가 min heap 원소보다 크다?
= 마지막 부모노드에 달린 왼쪽 자식이 오른 자식보다 더 크다는 뜻

3. 바꿔주기

4. print(max_heap[0][1]) -> min heap 모듈인 heapq를 tuple의 우선순위를 활용해 max_heap으로 바꿨기 때문

max_heap의 최소 값과
min_heap의 최대 값만을 비교하는 문제인 것과 왼쪽,오른쪽 자식을 heap으로 2개 나누는 것이 중요한 문제.
중간값의 원리를 잘 생각하기!
'''



