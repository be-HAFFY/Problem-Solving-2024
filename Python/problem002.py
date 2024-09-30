# Baekjoon Online Judge 1546

N = int(input())
scores = list(map(int, input().split()))
max_scores = max(scores)
sum_scores = sum(scores)

print(sum_scores * 100 / max_scores / N)
