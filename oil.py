print("Hello world")
n=int(input())
t=0
for i in range(1,n+1,1):
    l=int(input())
    ml=int(input())
    t+=(l*1000)+ml
tl=t/1000
print(int(tl))
tml=t%1000
print(tml)