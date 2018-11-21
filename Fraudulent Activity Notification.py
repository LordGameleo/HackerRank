import sys
#sys.stdin = open("in", "r")
n, d = map(int, raw_input().split())
arr = map(int, raw_input().split())


def findMedian(arr,d):
    if d % 2 == 0:
        for i in range(0,len(arr)):
            if medianAddress - arr[i] > 0:
                medianAddress -= arr[i]
            elif medianAddress - arr[i] <= 0:
                if medianAddress - arr[i] == 0:
                    return (i+i+1)*0.5
                else:
                    return i

    else:
        medianAddress += 1
        for i in range(0,len(arr)):
            if medianAddress - arr[i] > 0:
                medianAddress -= arr[i]
            elif medianAddress - arr[i] <= 0:
                return i

def activityNotifications(expen, d):
    notificationCount = 0
    checkArray = [0]*202
    for i in range(0,d):
        checkArray[expen[i]] += 1


    countAlert = 0

    for i in range(d,n):

        median = findMedian(checkArray,d)
        if 2*median <= expen[i]:
            countAlert += 1
        else:
            pass

        checkArray[expen[i-d]] -= 1
        if i+1 <n:
            checkArray[expen[i+1]] += 1



    median = findMedian(checkArray,d)
    if 2*median < expen[n-1]:
        countAlert += 1
    else:
        pass
    return countAlert

print activityNotifications(arr,d)
