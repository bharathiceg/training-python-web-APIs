#Write a Python program that takes three numbers as input and prints the largest among them.
n1=int(input("Enter number 1"))
n2=int(input("Enter number 2"))
n3=int(input("Enter number 3"))
if (n1>n2) and (n1>n3):
    print("The number 1 is bigger",n1)
elif (n2>n3):
    print("Number 2 is bigger",n2)
else:
    print("Number 3 is bigger",n3)
# Leap Year Checker:** Write a Python program that takes a year as input and determines if it is a leap year or not.
year=int(input("Enter the year to check leap yr: "))
if((year%4)==0 and (year%100 != 0)):
    print("leap year")
else:
    print("not a leap yr")
#

