#Binary Search
import sys
num_1 = int(input())

list_1 = list(map(int, input().split()))

num_2 = int(input())

list_2 = list(map(int, input().split()))

list_1.sort() # 오름차순으로 정렬

def binary_search(list_, target): #사용자 정의 함수
    left, right = 0, len(list_1) - 1 # 맨 왼 쪽과 오른 쪽 assign

    while left <= right: # 이 경우는 참일 경우인데 만약 left> right가 된다면 검색범위가 없음
        mid = (left+right)//2 #binary 알고리즘의 특성
        if target < list_[mid]: #오른 쪽것을 더이상 볼 필요가 없음
            right = mid - 1 # 검색범위를 줄임- binary 알고리즘
        elif target > list_[mid]: # 왼쪽 것을 볼 필요가 없음
            left = mid + 1 # 검색범위를 줄임 -binary 알고리즘
        else:
         return True #찾았다면 1 반환 -> 아래 if문의 조건문의 발동조건을 설정하기 위함.

for i in range(len(list_2)):
        if binary_search(list_1,list_2[i]): #list_2의 element가 list_1에 포함되어 있다면의 조건문
            print('1')                      #if문의 조건이 참이면 1을 print
        else :
            print('0')                      #if문의 조건이 거짓이라면 0을 print


