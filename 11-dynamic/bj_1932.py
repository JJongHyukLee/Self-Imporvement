import sys

sys.stdin = open('bj_1932.txt', 'r')


def max_path(row, col):
    if row == _size - 1:
        _memo[row][col] = _triangle[row][col] #맨 마지막은 자기 자신 반환

        return _memo[row][col] #맨 마지막도 memo에 저장해줌

    if _memo[row][col] is None:
        path_left = _triangle[row][col] + max_path(row + 1, col) #triangle =p_1, max_path = r
                                                                 #왼 쪽으로 가는경우
        path_right = _triangle[row][col] + max_path(row + 1, col + 1)
                                                                 # 오른 쪽으로 가는 경우

        if (path_left <= path_right):
            _memo[row][col] = path_right
        else:
            _memo[row][col] = path_left
        #왼 쪽, 오른 쪽 중 max 값을 _memo에 저장
    return _memo[row][col]


_triangle = []

_size = int(input())
_memo = [[None] * i for i in range(1, _size + 1)]
                    #i 만큼 memory -> 삼각형이 만들어짐
for _ in range(_size):
    _triangle.append(list(map(int, input().split())))
print(max_path(0, 0))
