import sys, heapq, math

INF = math.inf

V, E = map(int, sys.stdin.readline().split())
# int(sys.stdin.readline()) : 입력을 하나 받을 때
# map(int,sys.stdin.readline().split()) : 입력을 두 개이상 받을 때
source_number = int(sys.stdin.readline())

graph = [[] for _ in range(V + 1)]  # 1번 node는 사용하지 않기 때문

vertex_relaxing = [INF] * (V + 1)  # 1번 노드 사용 x
min_queue = []

# 이 위까지는 initialize 임.
for i in range(E):  # directed graph 구성
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])  # directed graph이기 때문

    # undirected graph라면 append를 u에 대해서, v에 대해서 해야함

def dijkstra(graph, start):

    vertex_relaxing[start] = 0  # 자기 자신은 비용 0
    heapq.heappush(min_queue, [0, start])  # 시작값을 0으로 초기화
    selected = set()

    while min_queue:
        current_cost, vertex_name = heapq.heappop(min_queue)
        selected.add(vertex_name)

        for v , w in graph[vertex_name]: #relaxing 과정
            if v not in selected: #shortest에 정해지지 않았다는 듯
                if vertex_relaxing[v] > vertex_relaxing[vertex_name] + w:
                    vertex_relaxing[v] = vertex_relaxing[vertex_name] + w
                    heapq.heappush(min_queue, [vertex_relaxing[v], v])

dijkstra(graph, source_number)

for i in vertex_relaxing[1:]:
    print(i if i != INF else "INF")
