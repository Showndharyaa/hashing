
#Program to identify the frequency of characters in an array/list

N = [2,1,4,3,5,2,4,1,5,3,1,2,4,5,3,2,1,2,3,4,5,3,4,2,1,5,1,2,3,4,5,2,3,4,1,4]
m = len(N)
freq={}

def frequency(N,m):
  for i in range(m):
    if (N[i] not in freq):
        freq[N[i]] = 1
    else:
        freq[N[i]] += 1
  return freq


frequency(N,m)
for i in list(freq):
    print (i, "->" , freq[i])
