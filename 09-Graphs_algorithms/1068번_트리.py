#leaf node -> 자식의 개수가 0개인 노드

#이진 트리는 포화 이진 트리 번호를 이용하면 1차원 배열로 쉽게 표현할 수 있다.

import sys

def dfs(parent_idx): #tree에 입력된 부모 노드 중 지우고 싶은 것의 idx를 받음

    tree[parent_idx] = -2 #여기선 부모 노드를 말하고 있는 것이거.
    for i in range(n): #트리 전체 반복
        if parent_idx == tree[i]: # 방금 지운 노드를 부모 노드로 하고 있는 친구가 있는지 확인.
                                  # tree의 index는 node number를 얘기하고 있는거임.
            dfs(i)  # i의 자식도 지움
# 지우고 싶은 parent_idx를 받고 그 것을 -2로 바꿔줌(삭제표시)
# tree 안 부모 노드를 지우고 싶기 때문에 line.9는 이해 ㅇ
#but parent_idx와 tree[i]의 관계는?
# tree[i] = 부모 node 번호.

'''
!!!! parent_idx를 부모 노드로 하는 tree[i]는 지울 node의 자식 노드임!

부모 노드가 삭제됐기 때문에 자식 노드들은 자연스레 없어져야함!
'''


'''
위의 말이 사실이 되려면 2가지 조건이 필요함

1. tree원소는 값을 받을수록 전에 받았던 값보다 크거나 같아야함
그러나 그런 말은 문제 어디에도 없음

2. 트리의 종류는 매우 많은데 이 문제는 포화 이진 트리로 한정지어서 1차원 배열로 품
그러나 그런 말은 문제 어디에도 없음

!!!!!
첫 째줄: 노드의 개수 N
둘 째줄 : 각 노드의 부모가 주어짐, 없으면(root) -1이 주어짐
셋 째줄 : 지울 노드의 번호

-> 의문 2번 해결 but 1번은 아직도 해결 안 됨

-> 그림 그려보면 1번 해결

이 해결은 무시
'''


n = int(input())

tree = list(map(int, sys.stdin.readline().split()))

#이진 트리는 포화 이진 트리 번호를 이용하면 1차원 배열로 쉽게 표현할 수 있다.

cut = int(sys.stdin.readline()) #지울 부모 노드의 idx 번호

dfs(cut)
cnt = 0

for i in range(n): # i=0~4까지 돌고 ,if문은 i=3,4일때 반응 ) 예제 1
    if tree[i] != -2 and i not in tree:
        cnt +=1
print(cnt)
#-2는 지운 노드, i(parent_node)의 자식이 트리 안에 없으면 리프 노드

# i not in tree = i(parent_node)를 부모로 하는 idx가 없으면
# 자식이 없다는 뜻

# parent_node_nuber = idx(i)

# tree의 원소가 -2아니고(-2는 지워졌다는 뜻) + 트리 원소 중 -2란 값을 가지는
#부모 노드의 number를 부모 노드로 하는 원소가 없다면
#leaf 노드임



