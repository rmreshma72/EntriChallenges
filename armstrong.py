#Checking whether a number is Armstrong or not
def armstrong(num):
    result=0
    l = len(str(num))
    while (num>0):
        rem=num%10
        result = result + rem**l
        num=num//10
    return result

def check(a,b):
    if (a==b):
        return True
    else:
        return False
    
#main
num=int(input("Enter a number:"))
r=check(num,armstrong(num))
if (r==True):
    print(num, "is an Armstrong number")
else:
    print(num,"is not an Armstrong number")

#print Armstrong numbers in a range
rge = int(input("Enter a range:"))
print("Armstrong numbers in between 1 to ", rge)
for i in range(1,rge+1):
    r=check(i,armstrong(i))
    if (r==True) :
        print(i, end=', ')

