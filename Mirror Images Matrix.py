r,c=map(int,input("enter :").split())
b=[]
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input("Enter :")))
    b.append(a)
for i in range(r):
    for j in range(c):
        print(b[i][j],end=" ")
    print()
