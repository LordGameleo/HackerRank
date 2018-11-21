a = raw_input()

flag = 1
length = len(a)
i = 0
while True:
    # print "i = ",i
    if i<len(a)-1:
        if a[i] == a[i+1]:
            a = a[:i] + a[i+2:]
            i = 0
        else:
            i += 1
    else:
        break
print "After 1 time = ",a
# print "a = ",a

if len(a):
    print a
else:
    print "Empty String"
