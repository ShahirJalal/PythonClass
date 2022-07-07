animals=["dog.mouse.cow","horse.tiger.monkey",
          "badger.lion.chimp","trok.cat.bee"]
# for i in animals :
#     if "cat" in i:
#         print("String found")
#     else:
#         print("String not found")


for i in animals:
    if 'cat' in i:
        print('String found')
        break
else:
    print('String not found')