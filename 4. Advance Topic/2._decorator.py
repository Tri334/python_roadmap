'''Decorator biasanya untuk mebuat string menjadi KAPITAL atau lowecase'''

teks = 'saya belajar PYTHON sambil melihat code iNi.'

print('====================')
'''Rubah awalan karakter menjadi huruf kapital seperti judul'''
judul = teks.title()
print(judul)


'''Rubah teks menjadi kalimat yang baik dan benar'''
print('====================')
kalimat = teks.capitalize()
print(kalimat)

'''Rubah teks menjadi KAPITAL SEMUA'''
print('====================')
kapital = teks.upper()
print(kapital)

'''Rubah teks menjadi lower semua'''
print('====================')
lower = teks.lower()
print(lower)