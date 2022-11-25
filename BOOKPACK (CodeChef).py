# cook your dish here
for i in range(int(input())):
    a,b,c=map(int, input().split())
    if b%c==0:
        int1=b//c
    else:
        int1=b//c+1
    print(a*int1)