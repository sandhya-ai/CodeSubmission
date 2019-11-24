b1 = 0
b2 = 0
b1strike = True
b2strike = False
input = [1,2,0,0,4,1,6,2,1,3]
for index,score in enumerate(input):
    ball=index+1
    if b1strike==True:
        b1+=score
        #print ("b1",b1)
    else:
        b2+=score
        #print ("b2",b2)
    if (score%2 !=0 and ball %6!=0):
        b1strike = not b1strike
        b2strike = not b2strike

print(b1,b2,b1+b2)
