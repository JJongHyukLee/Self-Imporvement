def selector(s:list,f : list):
    selected_act = 1
    ans = [selected_act]

    for act in range(2,len(s)):
        if s[act] >= f[selected_act]:
            print(act, '!')
            selected_act = act
            ans.append(selected_act)

    return ans

_s = [0,1,3,0,5,3,5,6,8,8,2,12]
_f = [0,4,5,6,7,9,9,10,11,12,14,16]

print(selector(_s,_f))