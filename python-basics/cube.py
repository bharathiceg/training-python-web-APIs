password= "baaru"
guess=""
count=0
attempts=3
out_attempt=False
while guess!=password and not(out_attempt):
    if count <= attempts:
        guess= input("Enter the password:")
        count= count+1
    else:
        out_attempt=True
if out_attempt == True:
    print("please try again")
else:
    print("this is you correct password")
