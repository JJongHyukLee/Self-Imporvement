import sys

sys.stdin = open('bj_5585.txt', 'r')

def selector(s:list,f : list):
    selected_act = 1
    ans = [selected_act]

    for act in range(2,len(s)):
        if s[act] >= f[selected_act]:

            selected_act = act
            ans.append(selected_act)

    return ans

n= int(input())

money = 1000-n
result = 0

result += (money //500)
money %= 500

result += (money // 100)
money %= 100

result += (money // 50)
money %= 50

result += (money // 10)
money %= 10

result += (money // 5)
money %= 5

result += (money // 1)
money %= 1

print(result)