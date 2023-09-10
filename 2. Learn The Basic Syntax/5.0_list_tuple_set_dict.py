''' Perbedaan
- List
- Tuple
- Set
- Dict
'''


''' List itu adalah array, data bisa duplikat'''
sebuah_list_kosong = []
list_berisi = [123,'abc','sotong']
print(list_berisi)
list_berisi.append('kucing')
print(list_berisi)

''' Tuple isinya tidak bisa di edit, data bisa duplikat'''
sebuah_tuple_kosong = ()
#  Cara menambah data di tuple? dengan cara membuat tuple baru
sebuah_tuple = ('Ayam','Babi','Kucing')
data_baru = 'Kelinci'
tuple_baru = sebuah_tuple + (data_baru,) 
print(tuple_baru)
print('============')

''' Set isinya bisa di edit, data bisa duplikat'''
set_kosong =set()
set_kosong.add('sesuatu')
set_kosong.add('kelinci')
print(set_kosong)

print('============')
set_kosong.remove('sesuatu')
print(set_kosong)
set_baru = {False,True}
set_kosong.update(set_baru)
print(set_kosong)

print('============')
ambil_index  = set_kosong.pop() # Hilangkan/ambil index pertama
print(ambil_index)
print(set_kosong)

print('============')
set_kosong.clear()
print(set_kosong)


''' Dictionary berisi Key & Value hampir dimana Key tidak bisa duplikat'''

dict_kosong = {}
dict_kosong['Binatang'] = 'Kelinci'
dict_kosong['Binatang'] = [dict_kosong['Binatang']] + ['Buaya'] # Menambah isi dictionary sebelumnya dengan data baru
print(dict_kosong)
dict_kosong['Binatang'] = 'Anjing' # Replace Key 'Binatang' dengan data baru
''' Hati Hati dalam menambahkan data di key yang sama ''' 

dict_kosong['Binatang'] = ['Kancil','Buaya'] 
''' Bisa juga menambahkan data dengan cara ini ke keynya'''
dict_kosong['Binatang'].append('Singa')
print(dict_kosong)