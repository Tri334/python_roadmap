''' Hash table digunakan untuk memudahakn membuat key dan value data'''

hash_data = {}

'''Buatlah harga jual sayur dan buah berdasarkan jenis nya'''

data_harga = hash_data

data_harga['wortel'] = 30
data_harga['semangka'] = 300
data_harga['manggis'] = 900

print(data_harga)
print('==================')
del data_harga['semangka']
print(data_harga)

print('==================')
data_anggur = data_harga.get('anggur', False)  # If 'anggur' is not in the hash map, it returns False
print(data_anggur)

print('==================')
data_anggur = data_harga.get('semangka', 'Tidak ada semangka')  # If 'semangka' is not in the hash map, it returns 'Tidak ada semangka'
print(data_anggur)

