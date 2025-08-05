l=int(input("enter the number of elements in the list: "))

L=[]
sum=0
max=L[0]
min=L[0]
for i in range(l):
    L.append(int(input((f"Enter the {i}th number for list: "))))
    sum=sum+L[i]
print("the list is: ", L)
for num in L:   
    if(L[num]>max):
       max=L[num]
    if(L[num]<min):
        min=L[num]
print(f"{L[num]} is bigger") 
print(f"{L[num]} is smaller") 
avg=sum/l


print("the sum is :", sum)
print("the avg in thelist:", avg)
