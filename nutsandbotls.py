#Program to map nuts to their corresponding bolts

nuts = ["@","$","&","%","!","*"]
bolts = ["!","@","%","$","&","*"]

def nutsAndBolts(nuts,bolts):
  temp = dict()
  for i in range (len(nuts)):
    temp[nuts[i]] = 1

  for i in range(len(bolts)):
      if (bolts[i] in temp):
            nuts[i] = bolts[i]

  #return nuts

nutsAndBolts(nuts,bolts)

print("The matched nuts and bolts are : ")
for i in range (len(nuts)):
    print(nuts[i],end=' ')
print()
for i in range (len(bolts)):
    print(bolts[i],end=' ')
