import re
text=str(input("enter a raw string:"))
l=str(input("enter a string to search:"))
r1=re.search(l,text)
print(r1)
if(r1!=None):
    print("searching seccess...")
else:
    print("searching failure...")
    
