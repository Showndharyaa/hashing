#Program to compare if two arrays are equal

a1 = [10,50,5,9,7]
a2 = [9,5,10,7,50]
n = len(a1)
m = len(a2)

def isEqualArr(a1,a2,n,m):
    if (n != m):
        return False
    count = 0
    for i in list(a1):
        if i in a1:
            count += 1
        if (count != 0 and i in list(a2)):
            count -= 1
    if (count == 0) :
        return True

if (isEqualArr(a1,a2,n,m)):
    print ("Arrays are equal")
else:
    print("Arrays are not equal")
