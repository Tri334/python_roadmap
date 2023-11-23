'''List comprehension'''

'''Make a list'''

this_list = [1,2,3,4,5,6]
new_list =[]
for item in this_list:
    if item %2 != 0:
        new_list.append(item)
        
print(new_list)

'''Now use list comprehension'''

new_list = [ item for item in this_list if item %2 != 0 ]
print(new_list)

new_list = [ item for item in this_list if item %2 != 0 or item %4 == 0 ]
print(new_list)