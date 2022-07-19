from heapq import heappop, heappush
import math, sys

def dijkstra(graph,source):
    #initialize
    distance = {} #dictionary : key,value 저장 가능
    predecesoor = {}
    for node in graph.key(): #모든 vertex를 한 번씩 거침.
        distance[node] = math.inf #각 vertex의 거리 : 무한대 (초기화 단계)
        predecesoor[node] = None # 현재 vertex가 shortest path가 되기 위한 이전 vertex가 무엇인지 = None (초기화 단계)

    distance[source] = 0 #시작 source distance = 0

    selected = set() #모든 vertex가 set 함수 안에 들어가면 끝

    min_queue = [(0,source)] # (distance from source (v.d) , vertex name)

    while min_queue:
        distance_u, u = heappop(min_queue) #heapq.heappop(list) : 가장 작은 원소를 삭제 후 리턴
        selected.add(u) #set 함수에 값을 1개 추가할 땐 add / 여러개 추가할 땐 update

        # u v w = u vertex에서 v vertex까지 weight

        for v, w in graph[u].items():
            if v not in selected:
                if distance[v] > distance[u] + w: #현재까지 알려진 soruce로부터 v까지의 거리보다
                                                  #vertex u를 거쳐 v까지 도달하는게 더 짧다면

                    distance[v] = distance[u] + w #realxing (cost)
                    predecesoor[v] = u            #realxing (이 전에 거쳐야 하는 노드)
                    heappush(min_queue, (distance[v], v)) # min_queue에 v까지의 거리와 vertex name을 push

        return distance

V , E = map(int,sys.stdin.readline().split())

'''
int(sys.stdin.readline().split()) --> 한 개의 정수를 입력 받을 때

map(int,sys.stdin.readline().split())) --> 여러 개의 정수를 입력 받을 때
'''

source_number = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append([v,w]) # bellman과 달리 directed graph이므로 append는 한 번만.

graph_distance = dijkstra(graph,source_number)

for i in graph_distance[1:]:
    if i != math.inf:
        print(i)
    else:
        print("INF")


