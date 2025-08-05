# Write a Python program to swap the values of two variables without using a temporary variable.
n1=int(input("Enter the First number"))
n2=int(input("Enter the Second number"))
print("The numbers",n1,n2)
n2,n1=n1,n2
print("the swapped numbers",n1,n2)
#Write a Python program that takes an integer as input and prints whether it is even or odd.
if (n1/2==0):
    print("it is even")
else:
    print("odd")
#Write a Python program using a for loop to calculate the sum of the first N natural numbers, where N is taken as input from the user.
n=int(input("Enter the n number of natural numbers"))
sum=0

for nat in range(1,n):
    sum=sum+nat
    print (("the sum is:"),sum)
#Write a Python program using a while loop to calculate the factorial of a given number N.
fact=1
nat=1
while nat<=n:
    fact=fact*nat
    nat=nat+1
print ((f"the Factorial of the number {n} is:"),fact)

