num =int(input("Enter the number to be reversed: "))
rev = 0
#for i in range(len(str(num)),0,-1):
while(num>0) :
    last = num % 10
    rev = rev * 10 + last
    num = num // 10
print ("Reverse is :",rev)