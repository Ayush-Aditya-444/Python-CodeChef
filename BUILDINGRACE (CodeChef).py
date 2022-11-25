# cook your dish here
for i in range(int(input())):
    a,b,c,d=map(int, input().split())
    int1=a/c
    int2=b/d
    if int1<int2:
        print("Chef")
    elif int1==int2:
        print("Both")
    else:
        print("Chefina")