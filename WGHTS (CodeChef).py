# cook your dish here
for i in range(int(input())):
    a,b,c,d=map(int, input().split())
    if a==b+c:
        print("YES")
    elif a==c+d:
        print("YES")
    elif a==b+d:
        print("YES")
    elif a==b:
        print("YES")
    elif a==c:
        print("YES")
    elif a==d:
        print("YES")
    elif a==b+c+d:
        print("YES")
    else:
        print("NO")
    