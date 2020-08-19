def remove_elm(items, item):
    items.remove(item)
    return


my_list = [1, 3, 5]
my_list_copy = my_list.copy()

print(my_list)
print(remove_elm(my_list, 3))
print(my_list)
print(my_list_copy)
