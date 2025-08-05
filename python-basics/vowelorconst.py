#Write a Python program that takes a single character as input and determines whether it is a vowel or a consonant.

cha=input("enter the letter ")
cha = cha.lower()
if len(cha) == 1 and cha.isalpha():
    if cha in ("aeiou"):
        print(cha)
        print("It is a vowel.")
    else:
        print("It is a consonant.")
else:
    print("enter it correclty")
