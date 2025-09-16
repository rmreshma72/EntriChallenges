
#Assignmet 1 - Grading using conditional and logical operators

grade = 65

if grade > 90 and grade <= 100 :
    print ("Grade : A+")
elif grade > 80 and grade <= 90 :
    print ("Grade : A")
elif grade > 70 and grade <= 80 :
    print ("Grade : B+")
elif grade > 60 and grade <= 70:
    print ("Grade : B")
elif grade > 50 and grade <= 60 :
    print ("Grade : C+")
elif grade > 40 and grade <= 50 :
    print ("Grade : C")
elif grade <= 40 :
    print ("Grade : Fail")
else :
    print ("Invalid marks..")


