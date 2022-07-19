import sys

n = int(sys.stdin.readline())

answer= []

for _ in range(n):
    m = int(sys.stdin.readline())

    if m != 0:
        answer.append(m)
    else:
        answer.pop()
print(sum(answer))
