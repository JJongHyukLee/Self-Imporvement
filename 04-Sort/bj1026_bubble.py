# bubble_sort
import sys
sys.stdin = open('bj1026_in.txt','r')
def bubble_sort(unordered):        #정렬 안 된 list를 넘기겠다는 의미 ->오름차순정렬 사용자정의함수
    iteration = len(unordered) - 1 #iteration : 반복, list의길이 -1 만큼
                                   #마지막은 안 해도 되니깐 -1을 해준거임

    for i in range(iteration):     # i = 0 부터 iteration-1까지 실행 range의 끝은 포함x
        for k in range(iteration - i):
                                    #i=0일 때 last_index에 해당하는 값 결정
                                    #i=1일때  last_index-1에 해당하는 값 결정
                                    #i=2일 때 last_index-2에 해당하는 값 결정

            if unordered[k] > unordered[k + 1]:
                unordered[k], unordered[k + 1] = unordered[k + 1], unordered[k]
                                    #만약 인덱스 k에 해당하는 값이 k+1에 해당하는 값 보다 클 경우
                                    # 둘의 위치를 바꿈 -> 오름 차순
s=0

num = int(input())                  # Object num을 int형 변수로 입력받겠단 의미

list_1 = list(map(int, input().split()))  # map(변환함수, 순회 가능한 데이터)
                                          # input().split() ->  여러개의 입력을 공백을 기준으로 구분시켜줌
                                          # list로 감싸 list 취급을 받게 함.

list_2 = list(map(int, input().split()))

bubble_sort(list_1)                       # list_1에 오름차순 시킬 배열 전달.

for i in range(num):                     # list_2에 -를 붙여 음수의 값을 갖게 함
    list_2[i] = -list_2[i]

bubble_sort(list_2)                      #음수를 가진 list를 bubble_sort 시키면 내림차순이 됨.
for i in range(num):
    list_2[i] = -list_2[i]               #되돌려 놓음

for i in range(num):
    s += list_1[i] * list_2[i]          #최소값
print(s)

'''
for i in range(num):

    list_max = max(list_1)                # list_max라는 Object는 list_1에 속한 element 중 max를 뽑음

    list_min = min(list_2)                # list_min라는 Object는 list_2에 속한 element 중 min을 뽑음

    s += list_max * list_min              # 최대 * 최소가 되어야 S합이 가장 최소임

    list_1.pop(list_1.index(list_max))    #list_1.pop(?) -> list_1의 요소 중 ?라는 요소를 삭제함
                                          #list_1.index(?) -> list_1의 요소 중 ?라는 요소의 index를 반환
                                          #즉, list_1의 max의 인덱스 공간 자체를 삭제

    list_2.pop(list_2.index(list_min))
'''


'''
    # for loop
                in 뒤엔 항상 iterable object!
    !!!
    a = range(5)
    for i in a:
    print(i,end =' ')

    출력문 : 0 1 2 3 4 (end는 끝을 뭘로 마무리할지 지정) 

    for i in range(1,7,2):
    print(i,end=' ')

    출력문 : 1 3 5
    range(1,5) = 1234
    range(5) = 01234
    '''