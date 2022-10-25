print("hello world")
n=input()
n1=len(n)
for i in range(1,n1+1,1):
    if((int(n)%int(n[n1-i]))==0):
        print(int(n[n1-i]),end=" ")