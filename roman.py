n=int(input())
if(n<40):
    n1=int(n/10)
    for i in range(1,n1+1,1):
        print("X",end="")
    n2=int(n%10)
    if(n2<=3):
        for j in range(1,n2+1,1):
            print("I",end="")
    elif(n2==4):
        print("IV")
    elif((n2>=5)&(n2<=8)):
        print("V",end="")
        for k in range(1,n2-4,1):
            print("I",end="")
    elif(n2==9):
        print("IX")
if(n>=40):
    if(n<50):
        print("XL",end="")
    elif(n>=50)&(n<90):
        print("L",end="")
        n4=n-50
        if(n4<40):
            n5=int(n4/10)
            for z in range(1,n5+1,1):
                print("X",end="")
    else:
        print("XC",end="")
        
    n3=int(n%10)
    if(n3<=3):
        for x in range(1,n3+1,1):
            print("I",end="")
    elif(n3==4):
        print("IV")
    elif((n3>=5)&(n3<=8)):
        print("V",end="")
        for y in range(1,n3-4,1):
            print("I",end="")
    elif(n3==9):
        print("IX")

    
    
    
      
        

