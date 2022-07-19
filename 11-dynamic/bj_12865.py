import sys

sys.stdin = open('bj_12865.txt', 'r')


def knapsack(_capacity, item):

    if _capacity == 0 or item >= _number: # 남은 여유공간이 0 이거나
                                          #물품 수가 더 많거나 같을때(고려해야할 마지막물건일떄)
        memo[(_capacity,item)] = 0 #tuple로 저장.
        return 0

    if _weight[item] > _capacity: #아이템의 무게가 수용량보다 많을 때 -> 다음 아이템 고려
        memo[(_capacity,item)] = 0  #그 때 0 기입
        return knapsack(_capacity, item + 1) #return과 동시에 recursion

    if (_capacity, item) not in memo: #memo에 없던 새로운 식이라면
        with_the_item = _value[item] + knapsack(_capacity - _weight[item], item + 1)
        #item을 넣었을 경우, p_1 + r_n-1 이므로, 그 해당 아이템의 값 +
        #해당 아이템의 무게를 갖고 있는 여유공간에서 뺀 상태로 다시 recursion
        without_the_item = knapsack(_capacity, item + 1)
        #고려하는 아이템을 안 넣을 경우 그냥 다음 아이템 고려
        if with_the_item < without_the_item:
            memo[(_capacity, item)] = without_the_item
        else:
            memo[(_capacity, item)] = with_the_item
            # max 찾기
    return memo[(_capacity, item)]


_weight = []
_value = []
_number, capacity = map(int, input().split())
memo = {}
for i in range(_number):
    N, V = map(int,(input().split()))
    _weight.append(N) #인덱스 = item의 번호
    _value.append(V) #인덱스 = item의 번호
    # memo[(N,V)] = None
print(knapsack(capacity, 0)) #갖고 있는 여유공간과 0번 item을 고려하겠다는 의미
print(memo)