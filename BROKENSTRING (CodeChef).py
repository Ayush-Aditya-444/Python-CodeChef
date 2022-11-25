# cook your dish here
for i in range(int(input())):
    int1=int(input())
    str1=input()
    str2=str1[:len(str1)//2]
    str3=str1[len(str1)//2:]
    if str2==str3:
        print("YES")
    else:
        print("NO")