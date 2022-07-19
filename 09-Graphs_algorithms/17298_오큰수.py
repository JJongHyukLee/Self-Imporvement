from collections import deque
import sys
n = int(sys.stdin.readline())
list_item = list(map(int, sys.stdin.readline().split()))
#print(*list_item)
# list() = 괄호 안을 리스트로 저장해줌
# map(funtcion,iterable)
#function: 매개변수
#반복가능한 자료형 (리스트,튜플)
# 해당 자료형을 list혹은 tuple로 변환

#sys.stdin.readline() -> input을 string으로 받음
#split -> 스페이스바 or 엔터 기준으로 값을 나누어줌
        # -> 여러 개의 입력을 받을 때 구분하기 위함.
        # -> parameter(기본값:공백)을 기준으로 분할된 리스트를 만듦

'''
for i in range(len(a)):
...     a[i] = int(a[i])

a = list(map(int, a))

동의어

'''
NGE = [-1]*n
stack = []
'''
if stack:
    print(1) 
    
    출력 : print1
'''

for i in range(n):
    while stack and (stack[-1][0] < list_item[i]):
        #stack[-1][0]은 list 중 맨 뒤에 있는 요소를 가리키는 것임.
        sd, idx = stack.pop()
        NGE[idx] = list_item[i]
    stack.append((list_item[i], i))
    #print(stack)

print(*NGE)