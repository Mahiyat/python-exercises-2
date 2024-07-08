dict1 = {'age': 13, 'id': 12, 'address': 'Banani', 'course': 'Python'}
dict2 = {'address': 'Rupnagar', 'id': 25, 'course': 'MERN'}
dict1_common = {}
dict2_common = {}

for key, value in dict1.items():
  if key in dict2:
    dict1_common[key]=value
    dict2_common[key]=dict2[key]

print("Common items of the two dictionaries based on keys:")
common_items = list(dict1_common.items())
common_items.extend(list(dict2_common.items()))
print(common_items)