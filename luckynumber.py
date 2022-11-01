# Online Python compiler (interpreter) to run Python online.
d=input()
sum=0
sum1=0
for i in range(1,9,2):
    sum=sum+int(d[i-1])
    sum1=sum1+int(d[i])
p=sum*3
sum2=sum1+p
r=sum%10
if(r==0):
    print("lucky number")
else:
    print("Not a lucky number")


    
