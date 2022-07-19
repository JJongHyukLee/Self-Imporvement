n=int(input())

for i in range(n):
    s=list(map(str,input()))
    num=0
    for j in range(len(s)):
        if(s[j]=='('):
            num+=1
        else:
            num-=1
        if(num<0):    # 괄호가 )로 시작하면 정상적인 모양이 생기지 않기 때문에 바로 반복문을 나가도록 한다.
            break
    if(num==0):
        print("YES")
    else:
        print("NO")