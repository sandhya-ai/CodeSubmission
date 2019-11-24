input=[1,2,3,5,8,4,7,9,1,4,12,5,6,5,2,1,0,8,1]
# Stroing key as input number and value as repeating count
dict={}

for num in input:
    # if the number already in dict we increase the value count by 1
    if num in dict:
        dict[num]=dict[num]+1
    # if it is not in the dict, we increase value by 1
    else:
        dict[num]=1
print ("key as input and valuse as it is repeating count",dict)