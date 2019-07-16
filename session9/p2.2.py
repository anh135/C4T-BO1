items = ['red', 'blue', 'green', 'orange']

for i, item in enumerate(items):              
 if "e" in item :
     print(i + 1, ":", item)

i = int(input("position: "))
items.pop(i)     
for i, item in enumerate(items):              
 if "e" in item :
     print(i + 1, ":", item)