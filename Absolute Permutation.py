t = int(raw_input())


def absolutePermutation(arr,k):
    tempArr = []
    if k == 0:
        return arr
    elif arr[-1]%(2*k) != 0:
        return -1
    else:
        for i in range(0,arr[-1],2*k):
            for j in range(0,k):
                arr[i+j] += k
            for l in range(k,2*k):
                arr[i+l] -= k
    return arr

for j in range(0,t):
    n, k = map(int,raw_input().strip().split())
    arr = []

    for i in range(1,n+1):
        arr.append(i)

    answer = absolutePermutation(arr , k)
    if answer == -1:
        print -1
    else:
        print ' '.join(map(str, answer))
