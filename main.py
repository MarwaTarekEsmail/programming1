'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, HTML, CSS, JS.
Code, Compile, Run and Debug online from anywhere in world.

'''
print("welcome!")
print("start the game!")
coins=int(input("coins:"))
f=100000
while(coins>0):
    p1=int(input("p1: "))
    if(p1>=coins or p1>f*2):
        print("sorry, choose another num!")
        p1=int(input("p1: "))
        if(p1>=coins or p1>f*2):
            print("sorry, choose another num!")
            p1=int(input("p1: "))
            if(p1>=coins or p1>f*2):
                print(" sorry, choose another num!")
                p1=int(input("p1: "))
                if(p1>=coins or p1>f*2):
                    print("sorry, choose another num! ")
                    p1=int(input("p1:  "))
    coins=coins-p1
    if(coins==0):
        print("p1 wins!")
        break
    p2=int(input("p2: "))
    if(p2>coins or p2>f*2):
        print("sorry, choose another num!")
        p2=int(input("p2: "))
        if(p2>coins or p2>f*2):
            print("sorry, choose another num!")
            p2=int(input("p2: "))
            if(p2>coins or p2>f*2):
                print("sorry, choose another num !")
                p2=int(input("p2: "))
                if(p2>coins or p2>f*2):
                    print("sorry, choose another num !")
                    p2=int(input("p2: "))
                    if(p2>coins or p2>f*2):
                        print("sorry, choose another num!")
                        p2=int(input("p2: "))
    f=p2
    coins=coins-f
    if(coins==0):
        print("p2 wins!")
        
        
    

