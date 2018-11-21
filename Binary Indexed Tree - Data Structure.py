#This is used to get sum of a range of an array in O(log(n))
#Updation also takes place in O(log(n))

#Creation requires O(nlog(n))

# We will use two functions - getSumBITree of range and updateBITree

def updateBITree(BITree,index,value):
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


arr = [2,1,1,3,2,3,4,5,6,7,8,9]

BITree = createBITree(arr)

print "SUM of starting 6 elements is ",getSumBITree(BITree, 5)

BITree = updateBITree(BITree,3,6)

print "SUM of starting 6 elements is ",getSumBITree(BITree, 5)
