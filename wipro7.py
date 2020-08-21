#Problem: Vertical pyramid.
k=int(input("ENTER THE DEEPNESS OF PYRAMID:"))
for j in range(k):
    print("\n",end="")
    k=j
    for i in range(k+1):
        print("@",end=" ")
for j in range(k):
    print("\n",end="")
    k=k-1
    for i in range(k+1):
        print("@",end=" ")
