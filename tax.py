print("Hello world")
tax=0
i=int(input())
if(i>1000000):
    tax=(i*4)/100
    print(int(tax))
elif((i>500000)&(i<=1000000)):
    tax=(i*2)/100
    print(int(tax))
else:
    print("NIL")
