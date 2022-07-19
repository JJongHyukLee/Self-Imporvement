import sys

#sys.stdin = open('bj-1865.txt', 'r')

def bellman_ford(graph, source):
    distance = []#v.d
    predecessor = [] #v.파이

    for _ in range(len(graph)):
        distance.append(100) #negative를 감지하고 graph를 만들기 위함
                            # - 초기화를 무한대가 아닌 100으로
                            #connected가 아니기 때문
        predecessor.append(None) #predecessor 초기화
    distance[source] = 0

    for _ in range(len(graph) - 1):
        for u in range(1, len(graph)):
            for v, w in graph[u]:
                if distance[v] > distance[u] + w:
                    distance[v] = distance[u] + w
                    predecessor[v] = u

    for u in range(1, len(graph)):
        for v, w in graph[u]:
            if distance[v] > distance[u] + w:
                return print("YES")

    return print("NO")


tc = int(input())
for _ in range(tc):
    N, M, W = map(int, input().split())
    road = [[] for _ in range(N + 1)]
    # N : vetex 개수 (for 이용시 번호가 됨)
    # M : undirected edge의 개수
    # W : directed vetex 개수 (negative를 가짐)

    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        road[S].append([E,T])
        road[E].append([S, T])
        # undirected = 양방향 vetex이므로.. append가 2 개

    # S: s번부터  s번까지
    # E : e번까지 e번부터
    # T : weight  weight

    for _ in range(W):  # negative cycle이 있는 웜홀의 개수 만큼
        S, E, T = map(int, sys.stdin.readline().split())
        road[S].append([E, -T])

    #print(road)
# directed 이므로 append는 한 번만 써도 됨. ~vetex에서 ~vetex로
    bellman_ford(road, 0)
