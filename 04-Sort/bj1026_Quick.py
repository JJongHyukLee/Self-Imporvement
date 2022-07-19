# Quick_sort
import sys

sys.stdin = open('bj1026_in.txt','r')
def partition(unsorted, first, last): #전달할 정렬안된 lsit, 첫 index, 마지막 index
    pivot = unsorted[first]           #pivot : 첫 index
    left = first + 1                  # left pointer는 pivot 바로 다음.
    right = last                      # right pointer는 마지막 index

                                      # pivot을 기준 왼 쪽은 pivot보다 작아야 하고, 오른 쪽은 pivot보다 커야 함.
    while True:                       # 무조건 반복
        while unsorted[left] <= pivot and left < right:
            left += 1
                                      #index left가 pivot보다 작거나 같고, left<right 일경우 left+=1 ---> quick sort 특성
        while unsorted[right] > pivot and left >= first:
            right -= 1
                                      #index right가 pivot보다 크거나 같고 , left>= first일 경우 right -=1 ---> quick sort 특성
        if left < right:
            unsorted[left], unsorted[right] = unsorted[right], unsorted[left]
        else:                         # left pointer >= right pointer일 경우 while문 종료
            break
                                      # left<right일 경우 left,right의 위치를 바꿔즘 -> 그래야 위의 while문을 한 번 더 실행할 이유가 생김.
    unsorted[first], unsorted[right] = unsorted[right], unsorted[first]
                                      # Right가 가리키는 값을 pivot과 swap -> quick sort 특성.

    return right                      #pivot data가 들어간 위치의 index(right)를 반환.

def quick_sort(unsorted, first, last):#정렬안 된 list, 첫 index, 마지막 index(list의 길이)
    if first < last:                  #첫 index가 last index보다 작을 경우
        pivot_index = partition(unsorted, first, last)
                                      #pivot_index = partition 함수 호출 -> 2개의 sub-list로 바꾸고 pivot이 들어있는 위치의 index 반환.
        quick_sort(unsorted, first, pivot_index - 1)
                                      #quick_sort = last가 pivot index -> 왼 쪽의 sub-list -> 재귀함수
                                      #재귀함수 & if문 -> member가 한 가지의 sub-list가 남을 때까지 반복 -> 정렬됨
        quick_sort(unsorted, pivot_index + 1, last)
                                      #첫 index가 pivot+1 -> 오른 쪽의 sub-list
s=0

num= int(input())

list_1 = list(map(int, input().split()))

list_2 = list(map(int, input().split()))

quick_sort(list_1, 0, len(list_1) - 1) # 0,1,2,3,4를 해줘야 함. /마지막 index는 포함한다는 이야기인가?

for i in range(num):
    list_2[i] = -list_2[i]

quick_sort(list_2,0,len(list_2)-1) #이미 list_2는 음수가 되었으므로 내림차순으로 정렬됨

for i in range(num):
    list_2[i]= -list_2[i]
    s += list_1[i] * list_2[i]

print(s)

'''
for j in range(num):
    list_max = max(list_1)  # list_max라는 Object는 list_1에 속한 element 중 max를 뽑음

    list_min = min(list_2)  # list_min라는 Object는 list_2에 속한 element 중 min을 뽑음

    s += list_max * list_min  # 최대 * 최소가 되어야 S합이 가장 최소임

    list_1.pop(list_1.index(list_max))  # list_1.pop(?) -> list_1의 요소 중 ?라는 요소를 삭제함
                                        # list_1.index(?) -> list_1의 요소 중 ?라는 요소의 index를 반환
                                        # 즉, list_1의 max의 인덱스 공간 자체를 삭제

    list_2.pop(list_2.index(list_min))
'''