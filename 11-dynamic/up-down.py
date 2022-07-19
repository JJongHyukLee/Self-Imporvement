import math

def cut_rod_td(length):
    if length == 0:

        return 0

    if _memo[length] is None:

        max_revenue = -math.inf
        for i in range(1,length+1):
            print(i, _price[i], cut_rod_td(length - i))
            revenue = _price[i] + cut_rod_td(length-i)
            if revenue > max_revenue:
                max_revenue = revenue

        _memo[length] = max_revenue
        print(_memo)
    return _memo[length]
n= 1
_price = [0,1,5,8,9,10,17,17,20,24,30]
_memo = [None] * 11
_length = 4
