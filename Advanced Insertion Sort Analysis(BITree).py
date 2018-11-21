#This is used to get sum of a range of an array in O(log(n))
#Updation also takes place in O(log(n))

#Creation requires O(nlog(n))

# We will use two functions - getSumBITree of range and updateBITree

def updateBITree(BITree,index,value):
    #index here is where change is happening in arr
    #We take BIT as a array with start index as 1
    index += 1

    while index < len(BITree):
        BITree[index] += value
        # getting next index to update
        index += (index)&(-index)

    return BITree


def createBITree(arr):
    BITree = [0]*(1+len(arr))
    length = len(arr)
    for i in range(0,length):
        BITree = updateBITree(BITree,i,arr[i])

    return BITree

def getSumBITree(BITree, index):
    sum = 0

    #We take BIT as a array with start index as 1
    index += 1

    while index > 0:
        sum += BITree[index]
        #getting previous range sum
        index -= (index)&(-index)

    return sum


testCase = int(raw_input().strip())

for i in range(0,testCase):
    BITree = [0]*(10**7+1)
    length = int(raw_input().strip())
    arr = map(int,raw_input().strip().split())
    countSwap = 0
    for val in reversed(arr):
        BITree = updateBITree(BITree,val,1)
        countSwap += getSumBITree(BITree, val-1)
print arr
