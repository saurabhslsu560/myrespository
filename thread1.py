import re
text=str(input("enter a string:"))
k=str(input("enter a string to match:"))
r1=re.match(r''+k,text)
if(r1!=None):
    print("success..")
else:
    print("failure..")
