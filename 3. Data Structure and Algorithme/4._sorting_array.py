'''Belajar sort list & dictionary'''

sebuah_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

sebuah_array.sort()
print(sebuah_array)
'''Hilangkan duplicate'''
print('======================')
sebuah_array_unik = list(set(sebuah_array))
print(sebuah_array_unik)

'''Sorting dari belakang'''
print('======================')
sebuah_array_unik.reverse()
print(sebuah_array_unik)


'''Sorting dictionary berdasarkan Key'''
print('======================')
sebuah_dictionary = {'banana': 2, 'cherry': 5, 'apple': 3, 'date': 1}
sorted_dictionary_by_key = dict(sorted(sebuah_dictionary.items()))
print(sebuah_dictionary)
print(sorted_dictionary_by_key)

print('======================')
sorted_dictionary_by_key = dict(sorted(sebuah_dictionary.items(),reverse=True))
print(sebuah_dictionary)
print(sorted_dictionary_by_key)