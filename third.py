f1=open("demo.txt","r")
f2=open("demo1.txt","r")
f3=f1.read().split()
f4=f2.read().split()
print(f3)
print(f4)
z=len(f3)
print(z)
for i in f3:
    c=0
    l=0
    s=0
    for j in f4:
        l=l+1
        if(i!=j):
            c=c+1
    if(l==c):
        print(i)
        print(f3.count(i))
##    for j in range(0,z):
##        if(f3[j]==i):
##            del f3[j]
            

