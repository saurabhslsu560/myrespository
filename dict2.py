dict={1:"SAURABH",2:"UPADHYAY",3:21,4:"INFO TECH"}
print("name is:",dict.get(1)+" "+dict.get(2))
print("age is :",dict.get(3))
print("department is:",dict.get(4))
print(dict.items())
print(dict.pop(1))
print(dict.popitem())
Age=dict.setdefault(3)
print("age:",Age)
dict1={3:20}
dict.update(dict1)
print(dict)

