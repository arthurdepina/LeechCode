array = [2, 4, 6, 8, 10]
for i, j in enumerate(array):
    print(i, j)

remove_on_index = 2
new_array = [j for i, j in enumerate(array) if i != remove_on_index]
# new_array is composed of items (j) in the array if i's index (i) is
# different from theirs of the item to be removed (i != remove_on_idex)
print(new_array)