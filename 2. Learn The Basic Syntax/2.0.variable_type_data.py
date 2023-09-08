"""
    Tata penamaan variable
Setiap perusahaan mempunyai dokumentasi berbeda-beda dari penamaan Variable, Class, Function, dll
Berikut saya contohkan bagaimana cara menamai suatu vaiable
"""

"""
Rule:
· Berikan variable nama yang mudah di mengerti developer lain
· Jangan namai variable terlalu singkat
"""

# Contoh Penamaan Variable di Python versi saya
user_name = 'Andi'
user_email = 'andi@123.com'
user_age = 89

"""
Biasakan di mulai dari varibale apa di ikuti dengan child mereka
"""

# contoh lain
harga_barang = 90
harga_jual = 90
harga_beli = 129
nama_barang = 'Mobil'

"""
Disini saya menambahkan harga_ diikuti dengan childnya sehingga developer tau bahwa varibale itu berisi int/float/decimal
"""

"""
Variable di Python bisa berisi macam macam dimulai dari String,Int,Float,Array,Object,Class,Function dll
"""

ini_int = 1
ini_bisa_float_bisa_decimal = 1.2
ini_string = 'Hallo'
ini_array = []
ini_dictionary = {'key':'value','user_name':'andi','user_discord_name':'andi_x123'}
ini_boolean_true = True
ini_boolean_tapi_false = False
ini_set = {'Ayam','Sapi','Kerbau'}
ini_frozenset = frozenset({"apple", "banana", "cherry"}) # Biasanya digunakan pada codingan Machine Learning (AI)

"""
Isi suatu Variable bisa dirubah sesuai urutan
"""

ini_int = 1
print(f'ini_int = {ini_int}') # 1
ini_int = 'Hallo'
print(f'ini_int = {ini_int}') # 'Hallo

# Berhati hati dalam mengisi varibale, dapat di permudah dengan memakai nama variable yang jelas
# Cara menggunakan Variable jika ingin diganti

"""
Saya menamakan variable seperti ini untuk memudahkan pencarian dengan filter rumah_xxx
kalau ingin prefix panjang_rumah, lebar_rumah juga bisa sesuai style masing masing
"""
rumah_panjang = 9
rumah_lebar = 10
rumah_luas = rumah_panjang * rumah_lebar # 9 * 10
print(f'luas : {rumah_luas} m2') # 90
rumah_panjang = 20
rumah_luas = rumah_panjang * rumah_lebar # 20 * 10
print(f'luas setelah variable di ganti: {rumah_luas} m2') # 200
