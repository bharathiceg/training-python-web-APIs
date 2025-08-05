
#Write a Python program using a for loop to print the multiplication table of a given number N.
N=int(input("Which number table u want : "))
n=12
for i in range(1,n+1):
    Mul=N*i
    print(f"{N}*{i}={Mul}")

#Write a Python program using a while loop to count the number of digits in a given integer N.
M=int(input("Enter the number with more than 3 digits  u want : "))
count=0
while M>0:
    M=M//10
    print(M)
    count=count+1
print("The digits in the num:",count)
#Fibonacci Sequence: Write a Python program using a for loop to generate the Fibonacci sequence up to a given limit N.
a=0
b=1
print(a,b)
for k in range(N):
   a,b= b,b+a
   print(b,end=' ')
