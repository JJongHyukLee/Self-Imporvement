import math

def cut_rod_td(length):
    for i in range(1,length+1):
        max_revenue = -math.inf
        for j in range(1, i+1):
            revenue = _price[j] + _memo[i-j]
            if max_revenue < revenue:
                max_revenue = revenue
        _memo[i] = max_revenue

    return _memo[length]

_price = [0,1,5,8,9,10,17,17,20,24,30]
_memo = [0] * 11
_length = 8
print(cut_rod_td(_length))

print(_memo)