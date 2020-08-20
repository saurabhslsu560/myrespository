import re
text="abc@gmail.com xyz@yahoo.com lmn@gmail.com"
print(re.findall("@\w+",text))
print(re.findall("@(\w+)",text))
print(re.findall("\w+@",text))
print(re.findall("(\w+)@",text))
print(re.findall("@\w+.\w+",text))
print(re.findall("@.\w+",text))
print(re.findall(".@\w+.@",text))




