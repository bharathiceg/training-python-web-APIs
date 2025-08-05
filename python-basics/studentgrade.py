#Write a Python program that takes a student’s percentage as input and prints their corresponding grade according to 
# the following criteria: – 90% or above: A+ – 80-89%: A – 70-79%: B – 60-69%: C – Below 60%: Fail
stud1= int(input("enter the students percentage: "))
if(stud1>=90):
    print("A+")
elif(stud1 >=80):
    print("A")
elif(stud1 >=70):
    print("B")
elif(stud1 >=60):
    print("C")
else:
    print("Fail")