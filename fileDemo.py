f=open("demo.txt","r")
f1=f.readlines()
for i in f1:
    if(float(i)>25.0):
        print(i)
