def cloning(grid):
    newGrid = []
    for i in range(0,len(grid)):
        temp = []
        for j in range(0,len(grid[0])):
            temp.append(grid[i][j])
        newGrid.append(temp)
    return newGrid


def getArea(grid,i,j):
    flag = 1
    size = 0
    d = 1
    while True:
        if d+i < len(grid) and i-d >= 0:
            if d+j < len(grid[0]) and j-d >=0:
                if grid[d+i][j] == 1 and grid[i][d+j] == 1 and grid[i-d][j] == 1 and grid[i][j-d] == 1:
                    size += 4
                    d += 1
                else:
                    break
            else:
                break
        else:
            break
    return size+1


def getPlusCenter(grid,length,n,m): #length can be odd
    add = []
    for i in range(length//2,n-length//2):
        for j in range(length//2,m-length//2):
            if grid[i][j] == 1:
                if getArea(grid,i,j) >= length*2 -1:
                    add.append([i,j])

    return add

def solution(grid,n,m):
    lengthPossible = []
    product =[]
    for i in range(1,min(n,m)+1,2):
        lengthPossible.append(i)


    for i in range(0,len(lengthPossible)):
        addPossible = getPlusCenter(grid,lengthPossible[i],n,m)
        # we are chosing address possible for this length
        for j in range(0,len(addPossible)):
            x = addPossible[j][0]
            y = addPossible[j][1]

            # now make altered grid for this possible plus....
            # will make new grid for chosen address Possible
            clone = cloning(grid)
            for s in range(0,len(grid)):
                print grid[s]
            clone[x][y] = 0
            for dist in range(0,lengthPossible[i]//2+1):
                # print "x+dist",x,dist,x+dist
                clone[x+dist][y] = 0
                clone[x][y+dist] = 0
                clone[x][y-dist] = 0
                clone[x-dist][y] = 0
            for s in range(0,len(grid)):
                print clone[s]


            # for given lengthPossible
            for k in range(i,len(lengthPossible)):
                addPossibleForInner = getPlusCenter(clone,lengthPossible[k],n,m)
                if len(addPossibleForInner)>0:
                    product.append((2*lengthPossible[k]-1)*(2*lengthPossible[i]-1))
                else:
                    pass
    return product



n,m = map(int,raw_input().strip().split())

grid = []

for _ in range(n):
    grid_item = raw_input()
    grid.append(grid_item)

newGrid = []
for i in range(0,n):
    temp = []
    for j in range(0,m):
        if grid[i][j] == "G":
            temp.append(1)
        else:
            temp.append(0)
    newGrid.append(temp)


print solution(newGrid,n,m)
