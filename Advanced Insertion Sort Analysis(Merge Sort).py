#!/bin/python
def mergeSortGFG(arr):
    swap = 0
    arrL =[]
    arrR =[]
    if len(arr) >1:
        mid = len(arr)//2 #Finding the mid of the array
        L = arr[:mid] # Dividing the array elements
        R = arr[mid:] # into 2 halves

        L,swapL = mergeSortGFG(L) # Sorting the first half
        R,swapR = mergeSortGFG(R) # Sorting the second half
        swap += swapL
        swap += swapR

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                swap = swap + (len(R)-j)
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            swap = swap + (len(R)-j)
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1

    return arr, swap

#
# list = []
# for x in range(100000):
#     list.append(random.randint(-9,9))
#
# a = mergeSortGFG(list)
t = int(raw_input().strip())
# t = 1
for t_itr in xrange(t):
    n = int(raw_input().strip())
    arr = map(int, raw_input().rstrip().split())
    result,temp = mergeSortGFG(arr[::-1])
    print temp
    # print result
