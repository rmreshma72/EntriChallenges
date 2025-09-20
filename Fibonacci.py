prev=0
next=1
n= int(input("Enter the number of digits to be printed in Fibonacci series: "))
for i in range(1,n+1):
    print(prev)
    f=prev+next
    prev=next
    next=f