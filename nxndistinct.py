
#program to find out distinct numbers of an nxn matrix that repeats itself in each row

def findDistinctnumbers(mat,n):
  us=dict()
  for i in range(n):
    us[mat[0][i]] = 1

  for i in range(1,n):
    temp=dict()
    for j in range(n):
      temp[mat[i][j]] = 1

    for itr in list(us):
        if itr not in temp:
            del us[itr]
    if len(us) == 0:
      print ("No distinct numbers")
      break

  for itr in list(us):
        print(itr, end=' ')

mat = [[2,3,1,5],
       [7,9,6,4],
       [1,4,2,3],
       [5,3,1,2]]
n = len(mat)

findDistinctnumbers(mat,n)
