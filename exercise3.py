list1 = [3, 5, 7, 4, 8, 8]
list2 = [4, 9, 8, 7, 1, 1, 13]
set1 = set(list1)
set2 = set(list2)
common_elements = set1.intersection(set2)
common_elements_list = list(common_elements)
print("Common elements in the two lists: ", common_elements_list)
print("Sum of the common elements: ",sum(common_elements_list))