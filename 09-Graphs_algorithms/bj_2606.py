#bj_2606_BFS
from collections import deque
import sys

sys.stdin = open('bj_2606.txt', 'r')
def breadth_first_search(graph,root):

    visited = [] #방문했던 노드들을 기록하기 위한 빈 list 생성
    discovered = [] # 방문한 노드들의 이웃 노드를 기록하기 위한 빈 list 생성
    queue = deque([root]) # deque 사용방법
    discovered.append(root)# 2중 리스트 선언

    while len(queue) > 0: #queue가 빌 때까지
        node = queue.popleft() #queue에서 가장 먼저 들어간 node를 pop으로 뽑아내어 node에 저장한다.
        visited.append(node)  #뽑아낸 node를 visited 리스트에 추가한다 -> pop으로 뽑아낸다 = 방문한다.
        undiscovered = set(graph[node]).difference(set(discovered))
        #방금 방문한 node의 이웃 node들 중, queue에 들어간 적 없는 이웃 node를 찾아낸다.
        #전체 node (방문한 노드를 작은 graph라 보고) - queue에 들어간 적 있는 node = queue에 들어가지 않은 새로운 이웃 node
        if len(undiscovered) > 0:
            for elem in sorted(undiscovered): #sorting을 하고나서 for문 실행
                queue.append(elem)
                discovered.append(elem)
        #방금 방문한 node의 이웃 node들 중, queue에 들어간 적 없는 이웃 node를 queue에 추가하고, queue에 추가했기 때문에 discovered에 기록한다.

    return visited #방문 순서에 대한 list 반환

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)] # 0번 index는 없으므로.

for _ in range(m): #인접한 node 채우기
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
#이웃 노드이기 때문에 31과 32를 위와같이 표현
cnt = len(breadth_first_search(graph,1))-1 # 감염된 node를 찾기 때문에 감연시킨(시작 노드는 제외한다.)
print(cnt)