import re
text="ab12-06-2003xy 31-01ab-1983ab 22-03-2019xy"
r1=re.findall(r'\d{2}-\d{2}-\d{4}',text)
print(r1)
