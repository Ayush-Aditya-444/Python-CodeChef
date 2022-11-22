# cook your dish here
for i in range(int(input())):
    a,b=map(int, input().split())
    if a%b!=0:
        print("No")
    elif (a//b)%2==0:
        print("Yes")
    else:
        print("No")