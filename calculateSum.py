# function to print sum
def returnSum(input):
    sum=0
    for i in input.values():
        sum=sum+i
    return sum


input={'Rick':85,'Amit':42,'George':53,'Tanya':60,'Linda':35}
print("Sum :",returnSum(input))