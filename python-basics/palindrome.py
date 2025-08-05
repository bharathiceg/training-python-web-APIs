#String Palindrome:** Write a Python function to check if a given string is a palindrome or not.
str1= input("enter the string to  check for palindrome")
print("the original string",str1)
rev=""
for char in str1:
    rev= char+rev
print("the reversed string",rev)
if(str1==rev):
    print("it is a palindrome")
else:
    print("not a palindrome")


