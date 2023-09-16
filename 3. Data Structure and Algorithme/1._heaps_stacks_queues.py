suatu_array = ['ABC','Something','20',1290,{'batu':['akik','macan','hitam','paras']}]


'''Masukan data baru paling depan'''

suatu_array = ['array baru'] + suatu_array 
print(suatu_array)
'''Ambil array paling belakang'''
array_paling_belakang = suatu_array.pop(-1)
print(array_paling_belakang)
'''Taruh data baru di array paling belakang'''
key_0 = next(iter(array_paling_belakang))
array_paling_belakang[key_0] = array_paling_belakang[key_0] + ['Data Baru Untuk Batu']
print(array_paling_belakang)
'''Masukan lagi data yang sudah di ambil ke paling depan'''
suatu_array = [array_paling_belakang] + suatu_array
print(suatu_array)
array_baru = [123,456]
print('==============================')
'''Masukan data baru setelah index ke x'''
suatu_array[1:1] =array_baru
print(suatu_array)
array_baru = [1,2,67]
suatu_array[5:5] =array_baru
print(suatu_array)
if suatu_array:
    print('not empty')

array_kosong = []
if not array_kosong:
    print('empty')
    
if array_kosong:
    print('empty')
else:
    print('Array perlu di isi')

