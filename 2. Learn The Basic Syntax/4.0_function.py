''' Selamat datang di function '''

''' Penamaan Function 
Setiap perusahaan mempunyai aturan penamaan sendiri
di sini kita ambil aturan dimana dimulai dari huruf kecil kemudian kata kedua dengan huruf besar
'''

# Deklarasikan suatu fungsi dengan parameter 'sisi'
def luasJajarPersegi(sisi):
    luas = sisi * sisi
    return luas

''' Mari Kita Coba '''
persegi_sisi = 20
persegi_luas = luasJajarPersegi(persegi_sisi)
print(persegi_luas,'m2')


''' Di dalam function bisa isi apa aja?
- Semua apa yang dibutuhkan sesuai kebutuhan mau
'''

''' Ada juga namanya void function yaitu tanpa parameter dan tanpa 'return' '''

def kembalikanLuasPersegi():
    print('Ini adalah luas persegi')

kembalikanLuasPersegi() #Langsung dipanggil seperti ini karena cuma print di terminal

''' Ingat!
- Selalu coba function yang telah dibuat untuk meminimalisasi error -
'''

''' Build in Function dari versi Python sendiri bisa di coba coba'''
    
    
''' 
Absolute -> merubah nilai apapun menjadi positif
'''
sebuah_float = -2.45
sebuah_int = -200
menjadi_positif = abs(sebuah_float)
print(menjadi_positif)
menjadi_positif = abs(sebuah_int)
print(menjadi_positif)

'''
Iterable Any -> mengecek apakah suatu variable kosong atau tidak
'''
sebuah_array = ['a','b','c']
array_kosong = []
print(any(sebuah_array))  # Mengembalikan True karena bisa di looping
print(any(array_kosong))  # Mengembalikan False karena kosong

sebuah_varibale = ''
print(any(sebuah_varibale))  # Mengembalikan False karena kosong

try:
    sebuah_varibale = None
    print(any(sebuah_varibale))  # Mengembalikan Error karena None bukan iterable
except Exception as err:
    print(err)

'''
Iterable All -> mengecek apakah suatu variable kosong atau tidak
'''
print(all(sebuah_array))  # Mengembalikan True karena bisa di looping
print(all(array_kosong))  # Mengembalikan True karena kosong

'''
Bin  -> konversi bilangan ke binary
'''
sebuah_bilangan = 123
print(bin(sebuah_bilangan))

'''
Enumerate -> mengembalikan objek dengan indexnya 
'''
array_buah = ['apel','jeruk','pir','nangka']
contoh_enum = enumerate(array_buah)
for index,value in contoh_enum:
    print(index,'|',value)