# cook your dish here
for i in range(int(input())):
    a,b=map(int, input().split())
    if a==b:
        print("Yes")
    else:
        if (a%2==0 and b%2==0) or (a%2!=0 and b%2!=0):
            print("Yes")
        else:
            print("No")