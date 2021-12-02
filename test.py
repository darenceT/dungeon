
pillars = ['A', 'I', 'E', 'P']

item_list = []

for item in pillars:
    if item not in item_list:
        item_list.append(item)
        print('add')
print(item_list)