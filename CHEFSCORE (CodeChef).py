for i in range(int(input())):
    (n,x,y)=map(int,input().split())
    if y>n*x or y%x!=0:
        print("NO")
    else:
        print("YES")