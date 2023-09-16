import re

teks = "harga ayam adalah 500 ribu, harga bebek adalah 600 ribu,harga hiu adalah 1500 ribu, harga bebek adalah 800 ribu"

'''Ambil kata binatang dan harganya'''
'''Gunakan chat gpt untuk mempermudah hidupmu'''
regex_pattern = re.compile(r'\b(\w+)\s+adalah\s+(\w+)\b')

matches = regex_pattern.findall(teks)

harga_hewan = {}
for data in matches:
    hewan, harga = data
    harga_hewan[hewan] = harga
    
print(harga_hewan)

'''Contoh lain bisa kreasikan sendiri'''