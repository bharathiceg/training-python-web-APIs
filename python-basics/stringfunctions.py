#String Reverse:** Write a Python function to reverse a given string and return the reversed string
name= input("enter the word to be reversed")
print("the original word",name)
rever=name[::-1]
print("reverse using ::-1",rever)
rev=""
for char in name:
    rev=char+rev
print("the reversed word is",rev)

# to convert the numbers list to string 
#Type Conversion:** Given a list of integers, write a Python program to convert each element of the list to a string.
number=[1,2,3,4]
strnum=[]
for num in number:
    strnum.append(str(num))
print("The list numbers",number)
print("the string numbers",strnum)
str1="bharthi"
str2="NA"
print(f"{str1}{str2}")
print(str1+str2)


    