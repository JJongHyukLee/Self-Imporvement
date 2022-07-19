import sys

sys.stdin = open('bj-1865.txt', 'r')


def bellman_ford(graph, source):
    distance = {}
    predecessor = {}
    for node in graph.keys():
        distance[node] = float('inf')
        predecessor[node] = None
    distance[source] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, w in graph[u].items():
                if distance[v] > distance[u] + w:
                    distance[v] = distance[u] + w
                    predecessor[v] = u
    for u in graph:
        for v, w in graph[u].items():
            if distance[v] > distance[u] + w:
                return False, distance, predecessor
    return True, distance, predecessor


tc = int(input())
for _ in range(tc):
    N, M, W = map(int, input().split())
    road = [[] for _ in range(N + 1)]
    # N : vetex 개수 (for 이용시 번호가 됨)
    # M : edge의 개수 ( directed = 1)
    # W : directed vetex 개수 (negative를 가짐)

    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        road[S].append([E,T])
        road[E].append([S, T])
        # undirected = 양방향 vetex이므로.. append가 2 개

    # S: S번 vetex에서 E vetex까지 T만큼의 weight
    # E : undirected = 양방향 이므로 E vetex에서 s vetex까지 T만큼의 weight
    # T : weight

    for _ in range(W):  # negative cycle이 있는 웜홀의 개수 만큼
        S, E, T = map(int, sys.stdin.readline().split())
        road[W].append(([E,T]))
# directed 이므로 append는 한 번만 써도 됨. ~vetex에서 ~vetex로

if bellman_ford(road, road[1]):
    print('Yes')
else:
    print('No')
