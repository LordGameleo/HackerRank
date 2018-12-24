s1 = raw_input().strip()
s2 = raw_input().strip()

def commonChild(s1,s2):
    A = [[0 for k in range(len(s1)+1)] for l in range(len(s2)+1)]
    # This Algo is using extra memory accessing time we can reduce it by using
    # enumerate
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                A[i][j] = A[i-1][j-1] + 1
            else:
                A[i][j] = max(A[i-1][j],A[i][j-1])

    return A[-1][-1]

print max(commonChild(s1,s2),commonChild(s2,s1))
