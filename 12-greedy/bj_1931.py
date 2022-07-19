import sys

#sys.stdin = open('bj_1931.txt', 'r')

def selector(s:list,f : list):
    selected_act = 1 #첫 번째 활동은 이미 select
    ans = [selected_act]

    for act in range(2,len(s)):
        if s[act] >= f[selected_act]: #s[2,3,4,5,6,.....] >= f[1]

            selected_act = act #예제로 보면 act =4 일대 select 됨  -> 다음 for문이 이어질 때 selelct = 4
            ans.append(selected_act)

    return ans

n= int(input())
acts = []
start=[0]
end=[0]
for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    acts.append((a,b)) #tuple로 저장
acts = sorted(acts, key = lambda x : (x[1],x[0]))
                                    #x[1](끝나는 시간으로 먼저 정렬, 그 뒤 시작 시간으로 정렬

for s,e in acts:
    start.append(s)
    end.append(e)
print(len(selector(start,end)))