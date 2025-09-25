#Create a list of 100 numbers
#Create seperate list of odd and even numbers
#Create list of numbers divisible by 3 and 5
num=[]
even=[]
odd=[]
multi=[]
for i in range(1,101):
    num.append(i)
print("Numbers are: ",num)
for i in num:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
    if(i%3==0 and i%5==0):
        multi.append(i)

print("Even numbers are:",even)
print("Odd numbers are:",odd)
print("Numbers Divisible by both 3 and 5 are :", multi)