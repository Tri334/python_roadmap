""" Terkadang kadang saat menerima dari suatu sumber
contoh: dari JSON
dari csv
dari excel
dari API
terkadang kadang tipe data tidak sesuai maka harus di convert
"""

'''
Contoh dari JSON
'''

data_json = {'nama' : 'Andi', 'umur' : '18' , 'menikah' : False}

print(data_json['umur'])
''' Harusnya umur itu tipenya int maka harus kita rubah" '''

tipe_umur = type(data_json['umur'])
umur = int(data_json['umur'])

data_json['umur'] = int(data_json['umur'])

''' Apakah contoh harus disebutkan semua? 
oo tentu sadja tidak, bisa ke roadmap dan lihat apa saja contohnya'''

''' Inti dari Tipe Data Conversion adalah
--- Bagaimana cara kita untuk mengubah suatu tipe data ke tipe data yang kita inginkan ---
'''