# cook your dish here
import math
for i in range(int(input())):
    a,b=map(int, input().split())
    if a>b:
        int1=(a-b)/2
    else:
        int1=(b-a)/2
    print(math.ceil(int1))
    