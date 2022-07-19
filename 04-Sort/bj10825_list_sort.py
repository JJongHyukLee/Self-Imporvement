import sys

n = int(sys.stdin.readline())
            #반복문으로 여러줄 입력받는 상황에서 반드시 input을 말고 sys.stdin.readline()을 씀
            #sys.stdin.readline()은 항상 str로 인식하기 때문에 3을 적어도 엔터를 누르면 3\n이 됨 -> 반드시 형변환 필요
a = []
            #빈 list(append를 진행할 list)

for i in range(n):
    a.append(sys.stdin.readline().split())
    #n번 여러 개 입력받음

a.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
    #10825문제 알고리즘.

for i in range(n):
    print(a[i])



