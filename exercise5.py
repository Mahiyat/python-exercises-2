list_1 = [4, 9, 8, 7, 5, 2, 13]
n = len(list_1)
list_1.sort(reverse=True)
print("After Sorting in Descending Order: ")
print(list_1)
diff = list_1[0]-list_1[n-1]
print("Subtraction of maximum and minimum numbers: ", diff)