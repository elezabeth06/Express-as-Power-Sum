def power(N,K,st):
    if N == 0:
        return 1
    if N<0:
        return 0
    c =0
    X = st
    while X**K<=N:
        c+=power(N-X**K,K,X+1)
        X+=1
    return c
T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    print(power(N,K,1))