pageh_doi = []
pageh_doi.append("Sita")
pageh_doi.append("Santi")
pageh_doi.append("Sinta")
print(pageh_doi[2])
print(len(pageh_doi))
pageh_doi.remove("Sita")
print(pageh_doi)
pageh_doi.pop(-1)
print(pageh_doi)
belanja_daftar = ["Ayam", "Babi", "Kecap", "Masako", "Micin"]
print(belanja_daftar[1])
print(belanja_daftar[0])
print(belanja_daftar[1:3])
makan = print(belanja_daftar[1:3])
print


'''Contoh'''
makanan = belanja_daftar[1:] # babi kecap
makan = " ".join(makanan)
makanan_subject = 'Saya makan ' + makan
print(makanan_subject)


new_makanan = ' '.join(belanja_daftar[1:])
subject_awal = 'saya makan '

print(subject_awal + new_makanan)
subject_awal = 'saya maling '
print(subject_awal + new_makanan)
