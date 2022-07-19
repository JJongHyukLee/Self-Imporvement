#Python_sort

num = int(input())

list_1 = list(map(int, input().split()))

list_2 = list(map(int, input().split()))

list_1.sort()

s=0

for i in range(num):

    list_max = max(list_1)                # list_max라는 Object는 list_1에 속한 element 중 max를 뽑음

    list_min = min(list_2)                # list_min라는 Object는 list_2에 속한 element 중 min을 뽑음

    s += list_max * list_min              # 최대 * 최소가 되어야 S합이 가장 최소임

    list_1.pop(list_1.index(list_max))    #list_1.pop(?) -> list_1의 요소 중 ?라는 요소를 삭제함
                                          #list_1.index(?) -> list_1의 요소 중 ?라는 요소의 index를 반환
                                          #즉, list_1의 max의 인덱스 공간 자체를 삭제
    list_2.pop(list_2.index(list_min))

print(s)