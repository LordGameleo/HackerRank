def rotAdd(x,y):           #x is row and y is column
    arr = [[0]*y]*x
    lengthX = len(arr)
    lengthY = len(arr[0])
    layers = []
    if lengthX >= lengthY:
        for i in range(0,lengthX//2+1):
            addArr = []
            k = i
            j = i
            lengthVerti = len(arr) - 1 - (k)
            lengthHori = len(arr[0]) - 1 - (j)
            while j <= lengthHori:
                addArr.append([k, j])
                j += 1

            j -= 1
            k += 1
            while k <= lengthVerti:
                addArr.append([k, j])
                if k<=lengthVerti:
                    k += 1
            k -= 1
            j -= 1
            while j >= i:
                addArr.append([k, j])
                j -= 1

            j += 1
            k -= 1
            while k > i:
                addArr.append([k, j])
                k -= 1
            if len(addArr) > 0:
                layers.append(addArr)
    else:
        for i in range(0,lengthY//2+1):
            addArr = []
            k = i
            j = i
            lengthVerti = len(arr) - 1 - (k)
            lengthHori = len(arr[0]) - 1 - (j)
            while k <= lengthHori:
                addArr.append([j, k])
                k += 1

            k -= 1
            j += 1
            while j <= lengthVerti:
                addArr.append([j, k])
                if j <=lengthVerti:
                    j += 1
            j -= 1
            k -= 1
            while k >= i:
                addArr.append([j, k])
                k -= 1

            k += 1
            j -= 1
            while j > i:
                addArr.append([j, k])
                j -= 1
            if len(addArr) > 0:
                layers.append(addArr)

    return layers


def transpose(arr):
    tempArr = []
    for i in range(0,len(arr[0])):
        temp = []
        for j in range(0,len(arr)):
            temp.append(arr[j][i])
        tempArr.append(temp)
        # print "tempArr @ iteration i = ",i," j = ",j, tempArr
    return tempArr

m,n = map(int,raw_input().strip().split())
k = int(raw_input().strip())
arr = []

for i in range(0,m):
    temp = []
    temp = list(map(int,raw_input().split()))
    arr.append(temp)

addRot = rotAdd(m,n)
num_layers = int(min(m,n)/2) + min(m,n)%2
layers = [[] for x in range(num_layers)]

if True:
    for i in range(0,min(m,n)//2+min(m,n)%2):
        addRotLayer = addRot[i]
        for j in range(0,len(addRotLayer)):
            layers[i].append(arr[addRotLayer[j][0]][addRotLayer[j][1]])

    # print layers
    for i in range(0,min(m,n)//2+min(m,n)%2):
        rotIndex = k % len(layers[i])
        layers[i] = list(layers[i][rotIndex:] + layers[i][:rotIndex])
    # print addRot

    for i in range(0,len(layers)):
        for j in range(0,len(addRot[i])):
            # print i,j,addRot[i][j][0],addRot[i][j][1], layers[i][j]
            arr[addRot[i][j][0]][addRot[i][j][1]] = layers[i][j]

for i in range(0,len(arr)):
    for j in range(0,len(arr[0])):
        print arr[i][j],
    print " "
