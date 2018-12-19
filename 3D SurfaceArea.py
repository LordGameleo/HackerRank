h,w = map(int,raw_input().strip().split())
arr = []

def surfaceArea(arr):
    surfaceArea = 0
    for i in range(0,len(arr)):
        surfaceArea += arr[i][0]
        for j in range(0,len(arr[i])-1):
            if arr[i][j+1]-arr[i][j] > 0:
                surfaceArea += arr[i][j+1]-arr[i][j]
            else:
                pass

    for i in range(0,len(arr)):
        surfaceArea += arr[i][-1]
        for j in range(len(arr[i])-1,0,-1):
            if arr[i][j-1]-arr[i][j] > 0:
                surfaceArea += arr[i][j-1]-arr[i][j]
            else:
                pass

    for j in range(0,len(arr[0])):
        surfaceArea += arr[0][j]
        for i in range(0,len(arr)-1):
            if arr[i+1][j]-arr[i][j] > 0:
                surfaceArea += arr[i+1][j]-arr[i][j]
            else:
                pass


    for j in range(0,len(arr[0])):
        surfaceArea += arr[-1][j]
        for i in range(len(arr)-1,0,-1):
            if arr[i-1][j]-arr[i][j] > 0:
                surfaceArea += arr[i-1][j]-arr[i][j]
            else:
                pass

    return surfaceArea + 2*(len(arr)*len(arr[0]))

for i in range(0,h):
    temp = []
    temp = map(int,raw_input().strip().split())
    arr.append(temp)

print surfaceArea(arr)
