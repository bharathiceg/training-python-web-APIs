#concatenate two tuples 
t1=(2,3,4,5,6)
t2=(1,7,8,9,0)
to= t1+t2
print(to)
t3 = list(to)
print(t3)
n=len(t3)

for i in range(n):
    for j in range((n-i-1)):
        if t3[j] < t3[j+1]:
            t3[j],t3[j+1] = t3[j+1],t3[j]
reverse=[]
for k in range(n-1,-1,-1):
    reverse.append(t3[k])
    t= tuple(t3)

print("the reversed list",reverse)
print("the reversed tuple",t)

print("the sorted tuple is :",t3)