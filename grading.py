
#Assignmet 1 - Grading using conditional and logical operators

sub1 = 78
sub2 = 85
sub3 = 92
sub4 = 74 
sub5 = 88 

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

print ("Total   :",total, "/500")
print ("Percentage :", percentage, "%")

if  percentage >= 90 and percentage <= 100 :
    print ("Grade : A+")
elif percentage >= 80 and percentage < 90 :
    print ("Grade : A")
elif percentage >= 70 and percentage < 80 :
    print ("Grade : B")
elif percentage >= 60 and percentage < 70:
    print ("Grade : C")
elif percentage >= 50 and percentage < 60 :
    print ("Grade : D")
elif percentage < 50 :
    print ("Grade : F")
else :
    print ("Invalid marks..")




