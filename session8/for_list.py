items = ['abc', 'def', 'ghi']


# for i in range(len(items)):
#     print(items[i])


# for item in items:
#     print(item)

for i, item in enumerate(items):              
 if "e" in item :
     print(i + 1, item)