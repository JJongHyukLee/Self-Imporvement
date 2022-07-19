#Bisect  -> binary search를 간단히 만듦
import bisect #bisect 모듈 사용

def bisect_search(bisect_list,target): #bisect_search
    index = bisect.bisect_left(bisect_list, target) # bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)
                                                    # 정렬된 순서를 유지하도록 a에 x를 삽입할 위치를 찾는다.
    if index < len(bisect_list) and bisect_list[index] == target: #주어진 list의 index에 벗어나지 않아야 하며
                                                                  #target과 list에 같은 값을 찾으면
        return True                                 # True를 반환
    else :
        return None                                 # 찾지 못할 경우 None을 반환
num_1 = int(input())

list_1 = list(map(int, input().split()))

num_2 = int(input())

list_2 = list(map(int, input().split()))

list_1.sort() # 오름차순으로 정렬

for i in range(len(list_2)):
    if bisect_search(list_1,list_2[i]): #반환받은 값이 0이냐 1이냐에 따라 1을 print할 것인지 0을 print할 것인지 결정
        print('1')
    else : print('0')

