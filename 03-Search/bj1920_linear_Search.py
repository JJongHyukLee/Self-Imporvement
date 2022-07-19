# Linear Search
import sys
n = int(input())                    #정수 n 받기 // input 함수는 문자열로 받기 때문에 int()를 붙여 int형으로 변환
a = list(map(int, input().split())) #map()함수 사용///list(map(적용시킬 함수, 적용할 값들))
                                    #map()함수 사용시 list로 반환해줘야 함

                                    #/// list(map(int, input().split()))
                                    #input으로 받는 입력을 쪼개고 int로 변환 후 list로 저장
n2 = int(input())
b = list(map(int, input().split()))

for i in range(len(a)):         #list의 index+1만큼 for문 동작 = list의 길이만큼 동작작
    if b[i] in a: print("1")    #alist에 b[i]가 들어있을 경우 print 1
    else: print("0")            #그렇지 않다면 print 0




