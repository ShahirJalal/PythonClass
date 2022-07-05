mydict = {'fruits': ['banana', 'apple', 'orange'],
         'vegetables': ['pepper', 'carrot'], 
         'cheese': ['swiss', 'cheddar', 'brie']}

# item = 'cheddar'
# for key in mydict.keys():
#     if item in mydict[key]:
#         print(key)

for key in mydict.keys():
    if key == 'cheese':
        for item in mydict['cheese']:
            if item == 'cheddar':
                print(item)