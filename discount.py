print("Hello world")
i=int(input())
p=int(input())
dis=0
if(i==1):
    if(p>1000):
        dis=p*0.1
elif(i==2):
    if(p>750):
        dis=(p*5)/100
else:
    if(p>500):
        dis=p*0.1
net=p-dis
print(int(net))