# cook your dish here
for i in range(int(input())):
    a,b,c,d=map(int, input().split())
    max1=max(a,b)
    max2=max(c,d)
    print(max1+max2)