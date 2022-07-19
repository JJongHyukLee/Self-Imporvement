import sys

sys.stdin = open('bj_2748.txt', 'r')

def fibonacci_td(n):
    if n<2:
        return n
    if _memo[n] is None:
        _memo[n] = fibonacci_td(n-1) + fibonacci_td(n-2)
    return _memo[n]

n=int(input())
_memo = [None] * 91 # 90은 안되고 91로 해야하는 이유 : Memo[0]과 memo[1]은
                    # None으로 채워져 있기 때문 index 0~91 = index 92개 0,1, 제외 90개
print(fibonacci_td(n))