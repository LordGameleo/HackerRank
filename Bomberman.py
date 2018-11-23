def fillNewBombs(numGrid):
    for i in range(0,len(numGrid)):
        for j in range(0,len(numGrid[i])):
            if numGrid[i][j] == -1:
                numGrid[i][j] = 1
            elif numGrid[i][j] == 1:
                numGrid[i][j] = 0
    return numGrid

def destructionAdd(numGrid,address):
    numGrid[address[0]][address[1]] = -1

    try:
        numGrid[address[0]+1][address[1]] = -1
        # print "changing at",address[0]+1,
    except IndexError:
        pass
    if address[0]-1>=0:
        numGrid[address[0]-1][address[1]] = -1
    try:
        numGrid[address[0]][address[1]+1] = -1
    except IndexError:
        pass
    if address[1]-1>=0:
        numGrid[address[0]][address[1]-1] = -1

    return numGrid


def blowBombs(numGrid):
    addDestructCenter = []
    for i in range(0,len(numGrid)):
        for j in range(0,len(numGrid[i])):
            if numGrid[i][j] == 0:
                addDestructCenter.append([i,j])

    # print "addDestructCenter = ",addDestructCenter
    for i in range(0,len(addDestructCenter)):
        numGrid = destructionAdd(numGrid,addDestructCenter[i])
    # print "addDestructCenter = ",addDestructCenter
    return numGrid

r,c,n = map(int,raw_input().strip().split())
grid = []
for i in range(0,r):
    grid.append(raw_input().strip())

# print grid

numGrid = []
for i in range(0,r):
    temp = []
    for j in range(0,c):
        if grid[i][j]==".":
            temp.append(-1)
        else:
            temp.append(0)
    numGrid.append(temp)


if n<2:
    printGrid = []
    for i in range(0,len(grid)):
        temp = []
        for j in range(0,len(grid[0])):
            if numGrid[i][j] == 0 or numGrid[i][j] == 1:
                temp.append('O')
            else:
                temp.append('.')
        printGrid.append(temp[:])

    for i in range(0,len(printGrid)):
        print "".join(printGrid[i])
    print ""

elif n>=2 and n<20:
    pass
else:
    n = 4 + n%8

for t in range(2,n+1):

    if t%2 == 0:
        numGrid = fillNewBombs(numGrid)
    else:
        numGrid = blowBombs(numGrid)

    printGrid = []
    # print ""

    for i in range(0,len(grid)):
        temp = []
        for j in range(0,len(grid[0])):
            if numGrid[i][j] == 0 or numGrid[i][j] == 1:
                temp.append('O')
            else:
                temp.append('.')
        printGrid.append(temp[:])

for i in range(0,len(printGrid)):
    print "".join(printGrid[i])
print ""
