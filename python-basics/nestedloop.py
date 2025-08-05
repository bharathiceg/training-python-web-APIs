#Write a Python program using nested loops to print the multiplication table from 1 to 10.
n=12
N=10
for i in range(1,N+1):
    for j in range(1,n+1):
      m=i*j
      print (f"({i}*{j}={m})")
s=5
for k in range(s):
       print(k * "*")