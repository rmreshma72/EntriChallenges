#List of prime numbers
a=int(input("Enter the starting number:"))
b=int(input("Enter the stopping number:"))
x=[]
if(a or b ==1):
    is_prime=False
for i in range(a,b+1):
    is_prime=True
    for j in range(2,i):
        if (i%j==0):
             is_prime=False
    if (is_prime):
        x.append(i)
print (x)