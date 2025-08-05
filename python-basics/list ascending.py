# program to print the descending order of numbers in a list 
n = int(input("enter the count of the numbers"))
numbers=[]
for k in range(n):
    numbers.append(int(input(f"enter the {k}th number:")))

print("the Actual numbers", numbers)
for i in range(n):
    for j in range(n-i-1):
        if numbers[j]<numbers[j+1]:
            numbers[j],numbers[j+1]= numbers[j+1],numbers[j]
print("the Descending order", numbers)

