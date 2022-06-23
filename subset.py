#program to identify if a2 is a subset of a1

a1 = [1,11,14,27,39,61]
a2 = [11,1,27,14]

def findSubset(a1,a2):
    temp=dict()
    for i in range(len(a1)):
        temp[a1[i]] = 1
    for j in list(temp):
        if j not in a2:
            del(temp[j])

    if (len(temp) == len(a2)):
        print("a2 is a subset of a1")
    else:
        print("a2 is not a subset of a1")

findSubset(a1,a2)
