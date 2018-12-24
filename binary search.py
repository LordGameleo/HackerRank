def binarySearch(arr,n):
    low = 0
    high = len(arr)-1
    flag = -1
    while True:
        mid = (low+high)//2
        if arr[mid] == n:
            flag = mid
            break
        elif arr[mid]<n:
            low = mid
        else:
            high = mid

        if mid == (low+high)//2:
            break


    if flag == -1:
        print "No Match"
    else:
        print "At index",flag

arr = map(int,raw_input().strip().split())
n = int(raw_input().strip())
binarySearch(arr,n)
