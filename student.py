f=open("demo1.csv","r")
f1=f.read().split()
for i in f1:
    f2=i.split(",")
    if(f2[0]=='R010'):
        for k in f2:
            print(k)
