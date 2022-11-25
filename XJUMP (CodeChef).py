# cook your dish here
for i in range(int(input())):
    a,b=map(int, input().split())
    int1=(a//b)+a%b
    if a<b:
        print(a)
    else:
        print(int1)