wizard_items = "milk, sugar, a package of salt, a bottle of water"
print(wizard_items)

wizard_list = ['milk', 'sugar', 'a package of salt', 'a bottle of water']
print(wizard_list)

print("wizard_list[0] = %s" % wizard_list[0])
print("wizard_list[2] = %s" % wizard_list[2])

wizard_list[2] = "2 pakcages of slat"
print(wizard_list)
print(wizard_list[2:4])

num_list = [1, 3, 5, 7]
name_list = ['tom', 'mike', 'eric', 'rose']
combine_list = [num_list, name_list]
print(combine_list)

print(wizard_list)
wizard_list.append("4 apples")
wizard_list.append("5 oranges")
print(wizard_list)

del wizard_list[3]
print(wizard_list)

list1 = [1, 2, 3, 4]
list2 = ['apple', "orange", "banana"]
list3 = list1 + list2
print(list3)
print(list1 * 5)
#------------------------------
fibs = (0, 1, 1, 2, 3, 5)
print(fibs)
print(fibs[2])

#----------------------------
