#Roman to Integer 
import sys
s=input("Enter a Roman number:").upper()
n=0

rom=['I','V','X','L','C','D','M']

try:
    for ch in s:
        if ch not in rom:
            raise ValueError()
except ValueError as e:
    sys.exit("Exiting the program because an invalid Roman number was found.")



#Converting Ones place
for o in range(len(s)-1,-1,-1): 
    if(s[o]=='X'):              # IX=9
        if(s[o-1]=='I'):
            n+=9
            s=s[:-2]
            break
    elif(s[o]=='V'):
        if(s[o-1]=='I'):        #IV=4
            n+=4
            s=s[:-2]
            break
        else:    
            n+=5
            s=s[:-1]
    elif(s[o]=='I'):
        n+=1
        s=s[:-1]

#Converting Tens place
for t in range(len(s)-1,-1,-1): #Converting Tens place
    if(s[t]=='C'):             #XC=90  
        if(s[t-1]=='X'):
            n+=90
            s=s[:-2]
            break
    elif(s[t]=='L'):            #XL=40
        if(s[t-1]=='X'):
            n+=40
            s=s[:-2]
            break
        else:
            n+=50
            s=s[:-1]
    elif(s[t]=='X'):
        n+=10
        s=s[:-1]

#Converting Hundreds place
for h in range(len(s)-1,-1,-1): 
    if(s[h]=='M'):          #CM=900
        if(s[h-1]=='C'):
            n+=900
            s=s[:-2]
            break
    elif(s[h]=='D'):        #CD=400
        if(s[h-1]=='C'):
            n+=400
            s=s[:-2]
            break
        else:
            n+=500
            s=s[:-1]
    elif(s[h]=='C'):
        n+=100
        s=s[:-1]

for th in range(len(s)-1,-1,-1):    #Converting Thousands place
    if s[th]=='M':
        n+=1000



print ("INTEGER:",n)   


