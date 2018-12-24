def minStep(x):
    stepArr = []
    for i in range(0,x+1):
        count = 0
        num = i
        count = num//5
        num = num%5
        count += num//2
        num = num%2
        count += num//1
        stepArr.append(count)
    return stepArr

def equal(arr,stepArr):
    minOp = 0
    minOp1 = 0
    minOp2 = 0
    minOp3 = 0
    for i in range(0,len(arr)):
        minOp1 += stepArr[arr[i]]
    arr = sorted(arr)
    minVal = arr[0]

    for i in range(0,len(arr)):
        arr[i] -= minVal
    for i in range(0,len(arr)):
        minOp += stepArr[arr[i]]

    for i in range(0,len(arr)):
        arr[i] += 1
    for i in range(0,len(arr)):
        minOp2 += stepArr[arr[i]]

    for i in range(0,len(arr)):
        arr[i] += 1
    for i in range(0,len(arr)):
        minOp3 += stepArr[arr[i]]

    print min(minOp,minOp1,minOp2,minOp3)

t = int(raw_input().strip())
for i in range(0,t):
    n = int(raw_input().strip())
    arr = map(int,raw_input().strip().split())
    stepArr = minStep(max(arr))
    equal(arr,stepArr)
