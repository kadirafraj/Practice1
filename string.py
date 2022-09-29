s=input("Enter String:")
a=list(s)
b=[]
b.append(a[0])
for i in range(0,len(a)-1):
    if a[i]!=a[i+1]:
        b.append(" ")
        i += 1
    b.append(a[i])
s1="".join(b)
c=s1.split(" ")
count=0
print(b)
for i in c:
    if len(i)>1:
        count+=1
print(count)