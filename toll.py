print("hello world")
km=int(input())
if(km<=1000):
    print("0")
elif((km>1000)&(km<=10000)):
    print("50")
elif((km>10000)&(km<=20000)):
    print("150")
elif((km>20000)&(km<=40000)):
    print("250")
elif((km>40000)&(km<60000)):
    print("350")
else:
    print("500")
    