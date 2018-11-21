import random
import timeit

mycode ='''
# My own
def mergeSort(list):
    swap = 0
    swapL = 0
    swapR = 0
    length = len(list)
    tempListL = []
    tempListR = []
    if length >1:
        mid = length//2 #Finding the mid of the array
        L = list[:mid] # Dividing the array elements
        R = list[mid:] # into 2 halves
        # print "L = ", L
        # print "R = ", R
        tempListL, swapL = mergeSort(L) # Sorting the first half
        tempListR, swapR = mergeSort(R) # Sorting the second half
    else:
        return list,swap

    listNew,swapM = sortedMerge(tempListL, tempListR)
    swap = swapL + swapR + swapM
    return listNew,swap



def sortedMerge(L,R):
    address1 = 0
    address2 = 0
    swap = 0
    k = 0
    arr = [0]*(len(L)+len(R))
    while address1 < len(L) and address2 < len(R):
        if L[address1] < R[address2]:
            arr[k] = L[address1]
            swap = swap + (len(R)-address2)
            address1 += 1
        else:
            arr[k] = R[address2]
            address2 += 1
        k+=1

    # Checking if any element was left
    while address1 < len(L):
        arr[k] = L[address1]
        swap = swap + (len(R)-address2)
        address1 += 1
        k += 1

    while address2 < len(R):
        arr[k] = R[address2]
        address2 += 1
        k += 1

    return arr, swap


list = []
for x in range(100000):
    list.append(random.randint(-9,9))

a = mergeSort(list)

'''

mycode2 ='''
#Geek For Geeks
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


list = []
for x in range(100000):
    list.append(random.randint(-9,9))

a = mergeSortGFG(list)

'''
# list = []
# for x in range(1000000):
#     list.append(random.randint(-9,9))

print timeit.timeit(setup = "import random",
                    stmt = mycode,
                    number = 10)/10

print timeit.timeit(setup = "import random",
                    stmt = mycode2,
                    number = 10)/10
