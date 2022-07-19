#bj_2606_BFS
from collections import deque
import copy
import sys
sys.stdin = open('bj_10026.txt', 'r')
def depth_first_search(graph, row, col):
    stack = [(row, col)]
    move = [[0, -1], [0, 1], [-1, 0], [1, 0]]

    color = graph[row][col] # graph를 2차원 배열로 만듦.
    #print(color) string 저장됨
    graph[row][col] = 'X' # 시작노드를 넘겨준다 = 방문했다 = 방문한 곳 X 표시

    while len(stack) > 0:
        row, col = stack.pop() #pop = 방문 //deque를 쓰는 BFS와 달리 stack을 쓰기 때문에 pop 사용
        for m in range(4): # 방문한 노드의 이웃 노드(상하좌우)를 살펴봄
            next_row, next_col = row, col
            next_row += move[m][0]
            next_col += move[m][1]
            print(next_row,next_col)
            if not check_move(graph, next_row, next_col, color): #만약 False가 전달되면 = search 대상이 없다면
                continue #아래 실행문을 실행하지 않고 for문을 돈다.
            stack.append((next_row, next_col)) #검토 대상이 되는 애들만 stack에 집어 넣는다.
            graph[next_row][next_col] = 'X' # 그 뒤 x를 표시한다.

def check_move(graph, row, col, color):
                                    # 방문한 노드의 이웃 노드인 '상하좌우' 노드들이 index를 넘는지(범위가 올바른지) 넘는다면 false 반환 ->검토 대상이 아니기 때문
                                     # 막 방문한 노드의 왼 오 상 하 노드를 한 번씩 check
                                     # 방문을 해도 되는 node인지 이 함수에서 check
    if row < 0 or row >= size:
        return False
    if col < 0 or col >= size:
        return False
    if graph[row][col] != color:     # 같은색깔이 아닐 경우 이 또한 false를 반환 해야함. -> 검토 대상이 아님
        return False
    if graph[row][col] == 'X':       # x 표시또한 false 반환 -> 검토 대상이 아님.
        return False
    return True

size = int(input())
graph = [list(input()) for _ in range(size)] # 2중 리스트 선언과 동시에 입력받기.

graph1 = copy.deepcopy(graph) #정상인
graph2 = copy.deepcopy(graph) #적록색약

count1 = 0 #정상인이 보는 구역을 count
count2 = 0 #적록색약이 보는 구역을 count

for i in range(size):
    for j in range(size):
        if graph2[i][j] == 'G':
            graph2[i][j] = 'R'
#2중 for문을 size*size 크기로 돌리면서, 'G'인 부분을 'R'로 바꿔줌 -> 적록색약은 red= green
for i in range(size):
    for j in range(size):
        if graph1[i][j] != 'X': # 정상인의 구역이 'X'가 아니라면
            depth_first_search(graph1, i , j) #DFS 실행 -> 실행할 graph와 시작 node 전달. ->인접한 같은 색깔이 X로 표시됨
            count1 += 1 #구역 하나를 X로 만들었으니 count+1
        if graph2[i][j] != 'X': #적록색약의 구역이 'X'가 아니라면
            depth_first_search(graph2,i,j) #DFS 실행 -> 인접한 같은 색깔을 x로 만들어줌
            count2 += 1 # 구역 하나를 X로 만들었으니 count+1

print(count1,count2)


