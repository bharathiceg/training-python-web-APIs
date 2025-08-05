# Write a Python program to count the number of even numbers in a nested list.
l1=[1,2,3,4,5,6,7,8,9]
print("the whole list is",l1)
n=len(l1)
count=0
for i in range(n):
    if ((l1[i]%2)==0):
        count+=1
print("the no of even numbers in the list: ",count)
max=[]
for j in range(n):
    print(j)
    for k in range(n-j-1):
        print(k)
        if (l1[k] > max):
            max = l1[k]
            
print("the maximum in the list",max)
