#Checking a number is Armstrong or not

def armstrong(num):
    result=0
    l = len(str(num))
    while (num>0):
        rem=num%10
        result = result + rem**l
        num=num//10
    return result

num=int(input("Enter a number:"))
if (armstrong(num)==num):
    print(num, "is an Armstrong number")
else:

    print(num,"is not an Armstrong number")
