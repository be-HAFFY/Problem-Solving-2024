# Baekjoon Online Judge 11660

N, M = map(int, input().split())

# 배열 선언, 초기화. 좌표가 1,1부터 시작하므로 0번째 배열은 사용 x
arr = [[0] * (N+1)]
D = [[0] * (N+1) for _ in range(N+1)]

for i in range(N): # 숫자 배열 입력받기
    row = [0] + [int(x) for x in input().split()] #맨 왼쪽 (x, 0) 비우고 자료 넣기
    arr.append(row)

for i in range(1, N+1): # 합 배열 만들기
    for j in range(1, N+1):
        D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + arr[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)
