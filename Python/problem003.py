# Baekjoon Online Judge 11659

N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [0]
temp = 0

for i in range(N):
    temp = temp + A[i]
    S.append(temp)

for i in range(M):
    f, e = map(int, input().split())
    print(S[e] - S[f-1])
