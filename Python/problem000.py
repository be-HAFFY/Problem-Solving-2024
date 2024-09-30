# Baekjoon Online Judge 2750

def merge(l, s1, e1, s2, e2):
    i, j, k, sorted = s1, s2, 0, [0]*(e2-s1+1)
    while(i<=e1 and j<=e2):
        if(l[i]<=l[j]):
            sorted[k] = l[i]
            i+=1
            k+=1
        else:
            sorted[k] = l[j]
            j+=1
            k+=1
    while(i<=e1):
        sorted[k] = l[i]
        i+=1
        k+=1
    while(j<=e2):
        sorted[k] = l[j]
        j+=1
        k+=1
    l[s1:e2+1] = sorted

def mergeSort(l, s, e):
    if(s>=e):
        return
    m = s+(e-s)//2
    mergeSort(l, s, m)
    mergeSort(l, m+1, e)
    merge(l, s, m, m+1, e)


N = int(input()) # 배열 길이
nums = list()

for i in range(N):
    nums.append(int(input()))

mergeSort(nums, 0, N-1)

# 출력문
print('=============')
for i in range(N):
    print(nums[i])

exit(0)
