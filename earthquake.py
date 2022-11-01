l=0
m=0
h=0
n=int(input())
if(n==0):
    print("No earth quake predicted")
elif(n<0):
    print("invalid input")
else:
    for i in range(1,n+1,1):
        r=float(input())
    if(r<5.4):
        l=l+1
    elif(r>=5.4)&(r<=7.0):
        m=m+1
    elif(r>7.0):
        h=h+1
    print(l)
    print(m)
    print(h)

