dict={10:"SAURABH",20:"UPADHYAY",30:21,40:"INFO TECH"}
dict1={3:20}
dict.update(dict1)
print(dict)
print(dict.values())
print('KEYS:')
for key in dict:
    print(key)
    print(key,end=" ")
print("\nVALUES:")
for key in dict:
    print(key)
    values=dict.get(key)
    print(values,end=' ')
