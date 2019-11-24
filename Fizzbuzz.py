num = int(input("Enter a number :"))

result=[]
for i in range(1,num+1):
    if i%3==0:
        result.append("Fizz")
    elif i%5==0:
        result.append("Buzz")
    elif i%3==0 and i%5==0:
        result.append("Fizzbuzz")
    else:
        result.append(i)
print(result)