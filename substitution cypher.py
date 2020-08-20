k=input("ENTER A STRING:")
print("OUTPUT:",end="")
for i in range(len(k)):
    d=ord(k[i])+2
    if(d==123):
        d=97
    if(d==124):
        d=98
    if(d==91):
        d=65
    if(d==92):
        d=66
    if(d==34):
        d=32
    print(chr(d),end="")
    



    
