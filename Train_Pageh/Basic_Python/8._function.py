def luasPersegi():
    None
def luasPersegiPanjang():
    panjang = 20
    lebar = 10
    luas = panjang * lebar
    return luas
luas_persegipanjang = luasPersegiPanjang()
print(luas_persegipanjang)
def luasPersegiPanjang2(panjang, lebar):
    luas = panjang * lebar
    return luas
luas_persegipanjang2 = luasPersegiPanjang2(lebar=1, panjang= 100)
print(luas_persegipanjang2)
array_panjang = [1, 2, 3, 4, 5]
array_lebar = [10, 20, 30, 40, 50]
def luasPersegiPanjangArray(panjang, lebar):
    luas = panjang * lebar
    return luas
# for i in range (len(minuman_dingin)):
#     print(i)
#     print(minuman_dingin[i])
#len = panjang suatu variabel
for p in range (len(array_panjang)):
    # print(array_panjang[p])
    # print(array_lebar[p])
    luas_parray = luasPersegiPanjangArray(lebar=array_lebar[p], panjang=array_panjang[p])
    print(luas_parray)



len_array_panjang = len(array_panjang)
print(len_array_panjang)
for i in range(len_array_panjang):
#     array_pangjang = array_panjang[i]
#     print(array_pangjang)
#     print('=========')
#     print(array_lebar[i])
    luas = luasPersegiPanjang2(lebar=array_lebar[i],panjang=array_panjang[i])
    print(luas)



    